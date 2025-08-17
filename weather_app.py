#!/usr/bin/env python3
"""
Weather App - Get current weather information for any city
Uses OpenWeatherMap API to fetch weather data
"""

import requests
import json
import sys
from datetime import datetime
from colorama import Fore, Style, init
from config import WEATHER_API_KEY, BASE_URL, DEFAULT_UNITS, TEMPERATURE_UNITS

# Initialize colorama for colored output
init(autoreset=True)

class WeatherApp:
    def __init__(self):
        self.api_key = WEATHER_API_KEY
        self.base_url = BASE_URL
        self.units = DEFAULT_UNITS
        
        if not self.api_key:
            print(f"{Fore.RED}❌ Error: No API key found!")
            print(f"{Fore.YELLOW}Please:")
            print("1. Copy .env.example to .env")
            print("2. Get a free API key from https://openweathermap.org/api")
            print("3. Add your API key to the .env file")
            sys.exit(1)
    
    def get_weather_data(self, city_name):
        """
        Fetch weather data from OpenWeatherMap API
        """
        try:
            # Construct the API URL
            complete_url = f"{self.base_url}?q={city_name}&appid={self.api_key}&units={self.units}"
            
            # Make the API request
            response = requests.get(complete_url, timeout=10)
            
            # Check if request was successful
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return {"error": "City not found"}
            elif response.status_code == 401:
                return {"error": "Invalid API key"}
            else:
                return {"error": f"API request failed with status code: {response.status_code}"}
                
        except requests.exceptions.RequestException as e:
            return {"error": f"Network error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
    
    def format_weather_data(self, data):
        """
        Format weather data for display
        """
        if "error" in data:
            return f"{Fore.RED}❌ Error: {data['error']}"
        
        try:
            # Extract weather information
            city = data['name']
            country = data['sys']['country']
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            description = data['weather'][0]['description'].title()
            wind_speed = data['main'].get('wind_speed', data.get('wind', {}).get('speed', 'N/A'))
            
            # Get temperature unit symbol
            temp_unit = TEMPERATURE_UNITS.get(self.units, "°C")
            
            # Format the output
            weather_info = f"""
{Fore.CYAN}🌤️  Weather Information for {city}, {country}
{Fore.WHITE}{'=' * 50}
{Fore.GREEN}🌡️  Temperature: {temperature}{temp_unit} (feels like {feels_like}{temp_unit})
{Fore.BLUE}☁️  Condition: {description}
{Fore.YELLOW}💧 Humidity: {humidity}%
{Fore.MAGENTA}🌪️  Pressure: {pressure} hPa
{Fore.CYAN}💨 Wind Speed: {wind_speed} m/s
{Fore.WHITE}📅 Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            return weather_info
            
        except KeyError as e:
            return f"{Fore.RED}❌ Error: Missing data in API response: {str(e)}"
        except Exception as e:
            return f"{Fore.RED}❌ Error formatting weather data: {str(e)}"
    
    def get_weather_for_city(self, city_name):
        """
        Get and display weather information for a city
        """
        if not city_name or not city_name.strip():
            return f"{Fore.RED}❌ Error: Please provide a valid city name"
        
        print(f"{Fore.YELLOW}🔍 Fetching weather data for {city_name}...")
        
        weather_data = self.get_weather_data(city_name.strip())
        return self.format_weather_data(weather_data)
    
    def set_units(self, units):
        """
        Set temperature units (metric, imperial, kelvin)
        """
        if units.lower() in ['metric', 'imperial', 'kelvin']:
            self.units = units.lower()
            unit_name = {
                'metric': 'Celsius',
                'imperial': 'Fahrenheit', 
                'kelvin': 'Kelvin'
            }
            print(f"{Fore.GREEN}✅ Temperature units set to {unit_name[self.units]}")
        else:
            print(f"{Fore.RED}❌ Invalid units. Use: metric, imperial, or kelvin")

def display_help():
    """Display help information"""
    help_text = f"""
{Fore.CYAN}🌤️  Weather App - Help
{Fore.WHITE}{'=' * 40}
{Fore.GREEN}Commands:
  help                 - Show this help message
  quit/exit           - Exit the application
  units <metric/imperial/kelvin> - Change temperature units
  <city name>         - Get weather for a city

{Fore.YELLOW}Examples:
  London
  New York
  Tokyo
  units imperial
  
{Fore.BLUE}Note: You need a free API key from https://openweathermap.org/api
"""
    print(help_text)

def main():
    """
    Main function to run the weather app
    """
    print(f"{Fore.CYAN}🌤️  Welcome to the Weather App!")
    print(f"{Fore.WHITE}Type 'help' for commands or enter a city name to get weather info.")
    print(f"{Fore.WHITE}Type 'quit' or 'exit' to exit the app.")
    print("-" * 60)
    
    # Initialize the weather app
    try:
        app = WeatherApp()
    except SystemExit:
        return
    
    # Main application loop
    while True:
        try:
            user_input = input(f"\n{Fore.WHITE}Enter city name (or command): ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"{Fore.GREEN}👋 Goodbye! Thanks for using Weather App!")
                break
            elif user_input.lower() == 'help':
                display_help()
            elif user_input.lower().startswith('units '):
                units = user_input.split(' ', 1)[1] if len(user_input.split(' ', 1)) > 1 else ''
                app.set_units(units)
            else:
                # Get weather for the city
                result = app.get_weather_for_city(user_input)
                print(result)
                
        except KeyboardInterrupt:
            print(f"\n{Fore.GREEN}👋 Goodbye! Thanks for using Weather App!")
            break
        except Exception as e:
            print(f"{Fore.RED}❌ An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
