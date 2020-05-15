import openweather 
from datetime import datetime 
import sys 
import os 
import requests 
import json 

# need to update to hide api key 
api_key = "d8d00d3f3137d7856f61036623a4b487"

ow = openweather.OpenWeather(cache=False)

def choose_emoji(conditions):
    return("placeholder")

def convert_cel(kelvin):
    return (kelvin - 273.15)

def make_url(city):
    url_key = 'http://api.openweathermap.org/data/2.5/weather?appid=' + api_key + "&q=" + city
    data = requests.get(url_key)
    json_data = data.json()
    return json_data


    # add emojis to the weather! So like sunny (sunny emoji) 
    # add limits to the temperature such as sunny! so happy 
    # cold so clown within that season 


#print(make_url("Mississauga"))