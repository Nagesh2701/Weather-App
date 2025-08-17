import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Default settings
DEFAULT_UNITS = "metric"  # metric for Celsius, imperial for Fahrenheit
TEMPERATURE_UNITS = {
    "metric": "°C",
    "imperial": "°F",
    "kelvin": "K"
}
