import requests

API_KEY = "aa26947dc88c57149df59f3612b223fd" 

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"{city} Weather: {temperature}°C, {weather}")
    else:
        print("City not found or Invalid API Key")

# Example Call
get_weather("Hyderabad")
