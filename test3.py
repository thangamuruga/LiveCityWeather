import requests
import pandas as pd
import os

Params = {
    "lat": "13.08784",
    "lon": "80.27847",
    "appid": "d5dae11bc2489ac50819f2d9ec8d9596",
    "units": "metric",
}

Params["lat"] = float(input("Enter the latitude\t"))
Params["lon"] = float(input("Enter the latitude\t"))

api_weather = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(api_weather, params=Params)

values = response.json()
# print(values)
# print(type(values))

for mains, temps in values["main"].items():
    # print(mains, temps)
    if mains == "temp":
        if temps < 30:
            print("Normal Temperature in your city")
        else:
            print("We are suggest you to carry water")
    elif mains == "humidity":
        if temps > 40:
            print("We are suggest you to carry Umbrella")
        else:
            print("Normal humidity in your city")
    elif mains == 'pressure':
        if temps > 1000:
            print("check the pressure value")
        else:
            print("normal pressure")
    else:
        pass
        


# 'main': {'temp': 31, 'feels_like': 34.36, 'temp_min': 31, 'temp_max': 31, 'pressure': 1008, 'humidity': 58}




df = pd.DataFrame(response)


df.to_excel("outputstorage3.xlsx", index=False)

file_path = os.getcwd()


