import requests

def city_name():
    # asking user for the city they want weather data for
    city = input("Enter the city name: ").strip()
    return city

def get_weather(city_name):
    api_key = "7cab71d942d5ad423838423135d9bab3"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # the data that should be returned
    request_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"
    response =requests.get(request_url)
    data = response.json()

    return data

def display_weather(weather_data):
    # specific data thats needed from the weather data
    city = weather_data["name"]
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    # the structure of how the data should be displayed
    print("-" * 30)
    print(f"Weather in {city.upper()}: ")
    print(f"Temperature: {temp}")
    print(f"Humidity: {humidity}")
    print(f"Condition: {description}")
    print("-" * 30)

def main():
    print("Welcome to the weather app")

    user_city = city_name()
    weather_data = get_weather(user_city)

    if weather_data.get("cod") == 200:
        display_weather(weather_data)
    else:
        message = weather_data.get("message", "City not found.")
        print(f"Error: {message.capitalize()}")

if __name__ == "__main__":
    main()