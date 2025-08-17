# 🌤️ Weather App

A Python-based command-line weather application that fetches real-time weather information for any city using the OpenWeatherMap API.

## 📋 Features

- **Real-time Weather Data**: Get current weather conditions for any city worldwide
- **Multiple Temperature Units**: Support for Celsius, Fahrenheit, and Kelvin
- **Detailed Information**: Temperature, humidity, pressure, wind speed, and weather conditions
- **Colorful Interface**: Beautiful colored output using emojis and colors
- **Error Handling**: Comprehensive error handling for API failures and invalid inputs
- **Interactive CLI**: User-friendly command-line interface

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- Internet connection
- OpenWeatherMap API key (free)

### Step 1: Clone or Download

Download the weather app files to your computer.

### Step 2: Install Dependencies

Open your terminal/command prompt, navigate to the weather_app directory, and run:

```bash
pip install -r requirements.txt
```

### Step 3: Get API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to your API keys section
4. Copy your API key

### Step 4: Configure API Key

1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Open the `.env` file and replace `your_api_key_here` with your actual API key:
   ```
   WEATHER_API_KEY=your_actual_api_key_here
   ```

## 🎮 Usage

### Running the App

Navigate to the weather_app directory and run:

```bash
python weather_app.py
```

### Commands

Once the app is running, you can use these commands:

- **Get Weather**: Simply type any city name
  ```
  London
  New York
  Mumbai
  Tokyo
  ```

- **Change Units**: Change temperature units
  ```
  units metric      (Celsius)
  units imperial    (Fahrenheit)
  units kelvin      (Kelvin)
  ```

- **Help**: Show help information
  ```
  help
  ```

- **Exit**: Exit the application
  ```
  quit
  exit
  ```

### Example Session

```
🌤️  Welcome to the Weather App!
Type 'help' for commands or enter a city name to get weather info.
Type 'quit' or 'exit' to exit the app.
------------------------------------------------------------

Enter city name (or command): London
🔍 Fetching weather data for London...

🌤️  Weather Information for London, GB
==================================================
🌡️  Temperature: 18°C (feels like 17°C)
☁️  Condition: Partly Cloudy
💧 Humidity: 65%
🌪️  Pressure: 1013 hPa
💨 Wind Speed: 3.5 m/s
📅 Updated: 2025-08-17 12:30:15

Enter city name (or command): units imperial
✅ Temperature units set to Fahrenheit

Enter city name (or command): quit
👋 Goodbye! Thanks for using Weather App!
```

## 📁 Project Structure

```
weather_app/
├── weather_app.py      # Main application file
├── config.py           # Configuration and settings
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .env               # Your API key (create this file)
└── README.md          # This file
```

## 🔧 Configuration

The app uses these configuration options:

- **API Key**: Set in `.env` file
- **Default Units**: Metric (Celsius) - can be changed in runtime
- **API Endpoint**: OpenWeatherMap Current Weather API
- **Timeout**: 10 seconds for API requests

## 🛠️ Troubleshooting

### Common Issues

1. **"No API key found" Error**
   - Make sure you created the `.env` file
   - Check that your API key is correctly set
   - Ensure there are no extra spaces in the API key

2. **"City not found" Error**
   - Check the spelling of the city name
   - Try using the format "City, Country" (e.g., "Paris, FR")

3. **"Invalid API key" Error**
   - Verify your API key on OpenWeatherMap website
   - Make sure the API key is active (can take a few minutes)

4. **Network Errors**
   - Check your internet connection
   - Verify that your firewall isn't blocking the connection

### Dependencies Issues

If you encounter issues with dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 📊 Weather Data

The app displays:

- **Current Temperature**: Actual and "feels like" temperature
- **Weather Condition**: Clear, cloudy, rainy, etc.
- **Humidity**: Percentage of humidity in the air
- **Atmospheric Pressure**: In hectopascals (hPa)
- **Wind Speed**: In meters per second
- **Location**: City name and country code

## 🔒 Privacy & Security

- API keys are stored locally in environment files
- No weather data is stored or transmitted elsewhere
- All API calls are made directly to OpenWeatherMap

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## ⚡ Quick Start

1. Get API key from OpenWeatherMap
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your API key
4. `python weather_app.py`
5. Type a city name and enjoy! 🌤️

---

**Made with ❤️ using Python and OpenWeatherMap API**
