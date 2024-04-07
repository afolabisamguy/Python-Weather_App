import requests
import json


def weather():
    print("Welcome to Samguy's Weather App")
    print("Enter the name of your city to check what the weather's like")

    city = input()
    # apicall = 'https://api.tomorrow.io/v4/weather/forecast?location=Kwara&apikey=U2WgVa4THIWIBFONFjV6GToKiDUVrTIZ'
    apicall = "http://api.weatherapi.com/v1/current.json?key=0dcae0d334a1406ea59144357242103&q="
    apicall += city
    apicall += "&aqi=yes"

    data = requests.get(apicall).json()

    location = data["location"]['name']
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]['text']
    print(f'location {location}')
    print(f'temperature {temperature}')
    print(f'condition {condition}')
    # print(data)

weather()
