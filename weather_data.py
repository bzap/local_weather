# @Linas Aleknevicius May 13/2020

import openweather 
import requests 
import json 

# need to update to hide api key 
api_key = "d8d00d3f3137d7856f61036623a4b487"

ow = openweather.OpenWeather(cache=False)

def choose_emoji(conditions):
    if (conditions == '01d'):
        return ':sunny:'
    elif (conditions == '02d'):
        return ':partly_sunny"'
    elif (conditions == '03d'):
        return ':cloud:'
    elif (conditions == '04d'):
        return ':cloud:'
    elif (conditions == '09d'):
        return ':cloud_rain:'
    elif (conditions == '10d'):
        return ':white_sun_rain_cloud:'
    elif (conditions == '11d'):
        return ':cloud_lightning"'
    elif (conditions == '13d'):
        return ':cloud_snow:'
    elif (conditions == '50d'):
        return ':fog:'

def country_flag(country):
    return ((":flag_" + country + ":").lower())

def convert_cel(kelvin):
    return (kelvin - 273.15)

def get_data(city):
    url_key = 'http://api.openweathermap.org/data/2.5/weather?appid=' + api_key + "&q=" + city
    data = requests.get(url_key)
    json_data = data.json()
    return json_data

#print(make_url("Mississauga"))
#data = ((get_data("Mississauga")))
#country_flag(data['sys']['country'])