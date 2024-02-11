import requests

# Replace YOUR_API_KEY with your actual API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY"

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather_data(weather_data):
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Weather Description: {weather_data['weather'][0]['description']}")

def main():
    city = input("Enter the name of the city: ")
    weather_data = get_weather_data(city)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()

#This code consists of three functions:
#get_weather_data(city): This function takes a city name as input and fetches the weather data from the OpenWeatherMap API.
#display_weather_data(weather_data): This function takes the weather data and displays the temperature, humidity, and weather description.
#main(): This function takes user input for the city name, calls get_weather_data() and display_weather_data(), and runs the app.
#To run the app, simply replace YOUR_API_KEY with your actual API key from OpenWeatherMap and execute the script.

