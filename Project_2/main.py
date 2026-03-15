import requests

# API Configuration
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# Function to get weather information
def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:

            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            print("\nWeather Information")
            print("----------------------")
            print("City:", city_name)
            print("Temperature:", temperature, "°C")
            print("Humidity:", humidity, "%")
            print("Condition:", description)

        else:
            print("City not found. Please try again.")

    except Exception as e:
        print("Error occurred:", e)


# Main Program
def main():

    print("===== Weather Checking System =====")

    city = input("Enter city name: ")

    get_weather(city)


if __name__ == "__main__":
    main()