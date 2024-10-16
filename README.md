# Python-Weather_App

## Overview

**WeatherApp** is a simple Python-based weather application that collects the name of your city from user input, makes an API call to a weather service, and retrieves the current weather details. The app displays the city name, temperature, and weather conditions in the console.

## Features
- **City-based weather retrieval**: Input your city name, and the app fetches the latest weather data.
- **Weather data**: Displays the temperature, weather conditions (e.g., clear, cloudy, rainy), and city location.
- **Real-time API integration**: Uses a third-party weather API to fetch real-time weather data.

## Files Description

### `weatherapp.py`
- The main script that handles:
  - Collecting the user's city name input.
  - Making the API call using the provided city name.
  - Parsing and displaying the weather data, including temperature and weather condition.

## How the App Works

1. **User Input**: The app asks you to input the name of the city.
2. **API Call**: The app constructs a URL using your city name and sends a request to a weather API.
3. **Display Weather**: The app fetches and displays the following information:
   - **Location**: Name of the city.
   - **Temperature**: Current temperature in Celsius or Fahrenheit (depending on API data).
   - **Weather Condition**: Current condition (e.g., clear sky, rainy, cloudy).

## Prerequisites

- **Python 3.x**
- **Requests** library for making API calls.

To install the `requests` library, run:
```bash
pip install requests
```

## API Setup

This app requires a third-party weather API (e.g., OpenWeatherMap). To use this app:
1. Sign up at a weather API service like [weatherapi.com] ).
2. Obtain an API key.
3. Update the script to include your API key in the API URL.

Example of the API URL structure:
```python
apicall = "https://api.weatherapi.com/v1/current.json?key={your_api_key}="
```

## How to Run the App

1. Clone this repository or download the project files.
2. Install the required dependencies using:
   ```bash
   pip install requests
   ```
3. Open the `weatherapp.py` file and ensure the API key is properly set in the API URL.
4. Run the script:
   ```bash
   python weatherapp.py
   ```
5. The app will prompt you to enter the name of your city. Enter the city, and it will display the current weather details.

## Example Output

```bash
Enter your city: New York
City: New York
Temperature: 15°C
Condition: Clear Sky
```

## Future Improvements

- Add error handling for invalid city names or failed API requests.
- Extend functionality to display more weather details (humidity, wind speed, etc.).
- Create a GUI version using a library like Tkinter.
- Allow users to switch between Celsius and Fahrenheit.

## License

This project is open-source and can be modified or distributed. Feel free to improve it or use it in your own projects.

---

Enjoy checking the weather with this simple WeatherApp!
