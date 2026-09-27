import requests


def get_weather(latitude, longitude):
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
    }

    weather_response = requests.get(weather_url, params=weather_params)
    weather_response.raise_for_status()

    result = weather_response.json()["current_weather"]
    # print("result=", result)
    return result


functions = {"get_weather": get_weather}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location. Infer the latitude and longitude yourself from the place name.",
            "parameters": {
                "type": "object",
                "properties": {"latitude": {"type": "number"}, "longitude": {"type": "number"}},
                "required": ["latitude", "longitude"],
            },
        },
    }
]
