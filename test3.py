import requests
import pandas as pd
import os

Params = {"city" : 'london'}

Params["city"] = input("Enter the city name")

api_url = 'https://api.api-ninjas.com/v1/geocoding'

response = requests.get(api_url,params= Params, headers={'X-Api-Key': 'F9tx2seTwD/pDYXlAlrMqQ==fNQVAusbN1ooGivJ'})

print(response.text)

coordinates = response.json()

print(type(coordinates))

for item in coordinates:
    if "latitude" in item:
        Params["lat"] = item["latitude"]
        print('Your City latitude is :', Params["lat"])
    if "longitude" in item:
        Params["lon"] = item["longitude"]
        print('Your City longitude is :',Params["lon"])
    if "name" in item:
        print("Your City Name : ", item["name"])

Params = {"lat": "13.08784", "lon": "80.27847", "appid": "d5dae11bc2489ac50819f2d9ec8d9596", "units": "metric"}


api_weather = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(api_weather, params=Params)

values = response.json()
print(values)
print(type(values))

for mains,temps in values["main"].items():
    print(mains , temps)
print('Kindly follow the Below Points :')
if values["main"]["temp"] < 30:
    print("Normal Temperature in your city")
else :
    print("We are suggest you to carry water")

if values["main"]["humidity"] > 50:
    print("We are suggest you to carry Umbrella")
else :
    print("Normal humidity in your city")


df =pd.DataFrame(response)


df.to_excel('outputstorage3.xlsx',index= False)

file_path = os.getcwd()


print("check your saved file at",file_path)


