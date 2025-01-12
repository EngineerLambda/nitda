# Interactive Mapping Application

## Overview
This project is an **interactive mapping application** built using **React** and **Vite**, with mapping functionalities powered by **Leaflet** and **Google Maps API** for tile layers. The application focuses on visualizing and interacting with location data for universities across Nigeria, providing users with comprehensive and real-time information about these institutions.

## Features
* **Dynamic Map Rendering**: Utilizes Leaflet for interactive map visualization.
* **Google Maps API Integration**: Fetches and displays tile layers, ensuring accurate and detailed mapping.
* **Secure API Management**: Manages API keys securely through environment variables.
* **University Location Data**: Loads data from an external JSON file containing details of Nigerian universities, including their latitude and longitude, fetched using the Google Maps API.
* **Interactive Markers**:
  * Dynamically placed markers representing university locations.
  * Popups displaying detailed information such as the institution's name and category.
* **AI-Powered Data Fetching**:
  * Retrieves live updates about universities, such as the current vice chancellor and session status, using an AI agent.
  * Features a chatbot that provides high-level, contextual responses to user queries about Nigerian universities.

## Use Cases

### For Prospective Students:
* Access information about school fees, available hostels, courses, faculties, and admission cut-off marks.
* Obtain course requirements and general admission details in real time.

### For Tourists, Parents, and Researchers:
* Stay informed about university updates.
* Explore and compare institutions based on personal or research needs.

## Challenges and Solutions
During the development of this project, a critical challenge arose: users had no direct means to inquire about specific details regarding universities. To address this:
* **Google Maps API Integration**: Enabled accurate location tracking of universities on the map.
* **AI-Powered Chatbot**: Added a chatbot feature capable of fetching real-time information about admission details, institution updates, and more, enhancing the user experience and making the application a comprehensive tool for educational research.

## Technologies Used
* **Frontend Framework**: React, Vite
* **Mapping Tools**: Leaflet, Google Maps API
* **AI Integration**: AI-powered agent for live updates and chatbot functionality
* **Data Management**: External JSON file for university data
* **Environment Variables**: Securely managing API keys

## Installation and Setup

1. Clone the repository:
```
git clone <repository-url>
```

2. Navigate to the project directory:
```
cd interactive-mapping-application
```

3. Install dependencies:
```
npm install
```

4. Create an `.env` file to securely store your Google Maps API key:
```
VITE_GOOGLE_MAPS_API_KEY=your_api_key_here
```

5. Start the development server:
```
npm run dev
```

6. Open your browser and visit `http://localhost:5173` to view the application.

## Contribution
We welcome contributions to enhance the application's functionality. To contribute:

1. Fork the repository and create your feature branch:
```
git checkout -b feature/your-feature-name
```

2. Commit your changes:
```
git commit -m "Add your message here"
```

3. Push to your branch:
```
git push origin feature/your-feature-name
```

4. Open a pull request for review.

## Future Enhancements
* Expand the dataset to include more institutions.
* Add more advanced filtering options (e.g., by region, institution type).
* Improve the chatbot's AI capabilities to handle complex queries.
* Integrate user authentication for a personalized experience.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Thank you for exploring our Interactive Mapping Application! If you have any feedback or suggestions, feel free to open an issue or reach out to us.