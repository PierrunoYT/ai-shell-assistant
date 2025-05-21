"""
Weather tool for AI CLI.
"""
import os
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

from ai_cli.tools.base import BaseTool

# Load environment variables
load_dotenv()


class WeatherTool(BaseTool):
    """A tool to get weather information."""
    
    name = "weather"
    description = "Get current weather information for a location"
    
    @property
    def parameters(self) -> List[Dict[str, Any]]:
        """Get the parameters for the weather tool."""
        return [
            {
                "name": "location",
                "description": "The city or location to get weather for",
                "type": "string",
                "required": True
            }
        ]
    
    def execute(self, args: Dict[str, Any]) -> str:
        """
        Execute the weather tool.
        
        Args:
            args: A dictionary containing the 'location' to get weather for.
            
        Returns:
            Weather information as a string.
        """
        location = args.get("location", "")
        
        if not location:
            return "Error: No location provided"
        
        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            return "Error: OpenWeather API key not found. Please set the OPENWEATHER_API_KEY environment variable."
        
        try:
            # Make API request to OpenWeatherMap
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract relevant information
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            # Format the response
            return f"""Weather in {location}:
- Condition: {weather_desc}
- Temperature: {temp}°C (feels like {feels_like}°C)
- Humidity: {humidity}%
- Wind Speed: {wind_speed} m/s"""
            
        except requests.exceptions.RequestException as e:
            return f"Error fetching weather data: {str(e)}"
        except (KeyError, IndexError) as e:
            return f"Error parsing weather data: {str(e)}"
