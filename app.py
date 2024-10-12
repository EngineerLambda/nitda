from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
date = f"{datetime.now():%Y-%m-%d}"

class KwaraInsts(BaseModel):
    in_session: str = Field(
        ..., 
        description="Determines whether the institution is currently in session, true, false or not available"
    )
    admission_ongoing: str = Field(
        ..., 
        description="Determines whether the institution's admission is currently ongoing"
    )
    vice_chancellor: Optional[str] = Field(
        None, 
        description="Full name of the school's vice chancellor, true, false or not available"
    )


template = """You are an AI assistant that uses provided information about universities in Nigeria to determine whether the school is in session whether admission is ongoing, and its vice chancellor name.
Information: {information}
The output should be formatted as JSON using the following format instructions:
{format_instruction}
To ensure the information is up-to-date, today's date is {date}. Make sure that none of the details include null, use 'not available' instead
Format the response accordingly."""

prompt = PromptTemplate(template=template, input_variables=["information", "format_instruction", "date"])
llm = GoogleGenerativeAI(model="gemini-pro")
parser = PydanticOutputParser(pydantic_object=KwaraInsts)

@app.get("/")
def home():
    return {"message": "Welcome to KwaraSAT"}

def format_search_result(result):
    # Process list of dictionaries to extract 'content' field
    if isinstance(result, list):
        return "\n\n".join([item['content'] for item in result if 'content' in item])
    return str(result)


@app.get("/live_details")
async def ai_result(inst_name: str):
    # search the web for necessary informations
    tool = TavilySearchResults()
    tavily_query = f"Latest news about {inst_name.lower()}, today's date is {date}"
    tavily_result = await tool.ainvoke({"query": tavily_query})
    
    # inference the llm
    formatted_info = format_search_result(result=tavily_result)
    chain = prompt | llm | parser
    output = await chain.ainvoke({
        "information": formatted_info,
        "format_instruction": parser.get_format_instructions(),
        "date": date
    })
    
    # ai response
    response = {
        "in_session": output.in_session,
        "admission_ongoing": output.admission_ongoing,
        "vice_chancellor": output.vice_chancellor or "not available"
    }
    
    return {"ai_response": response}

@lru_cache
async def load_web_data(query):
    tool = TavilySearchResults()
    inst_query = query
    result = await tool.ainvoke({"query": inst_query})
    
    return result
    

@app.get("/chatbot")
async def chatbot(query, inst_name):
    chat_template = """You are an AI agent that uses web sourced information of a university in Nigeria to answer user questions
        if the user question is a greeting, ignore the web details and respond to the greeting including introduction of yourself
        user question: {query}
        web_news: {web_data}
    """
    prompt = PromptTemplate(template=chat_template, input_variables=["query", "web_data"])
    llm = GoogleGenerativeAI(model="gemini-pro")
    web_result = await load_web_data(f"{query} {inst_name}")
    chain = prompt | llm
    response = await chain.ainvoke({"query": query, "web_data": format_search_result(web_result)})
    
    return {"ai_response": response}
    
    
