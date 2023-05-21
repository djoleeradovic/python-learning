import requests

API_KEY = "5df8201d20331e65bda908f3820d4ffe"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    print(f"Temp: {round(data['main']['temp']-273.15)}°C")
    print(f"Wind Speed: {round(data['wind']['speed'])}/kmh")
    print(f"Pressure: {round(data['main']['pressure'])}/mbar")
    print("----------------------")
else:
    print("Error")
