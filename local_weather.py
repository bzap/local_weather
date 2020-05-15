# @Linas Aleknevicius May 13/2020

import os 
import discord
from weather_data import choose_emoji, get_data, country_flag, convert_cel

TOKEN = 'NzEwNjQ4OTEzNjI2OTIzMTUz.Xr3hjw.YxSHQOQxn4pRGGjvPrn3e8K9Z1E'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} yolo')

@client.event
async def on_message(message):
    try: 
        if message.author == client.user:
            return
            
        elif message.content == ('!weather'):
            await message.channel.send(" > Invalid, use it in the format !weather <city>")

        elif (message.content == ('!weather here')) or (message.content == ('!weather Here')) :
            await message.channel.send(" > ur local weather sucks")
        
        elif len(message.content.split()) > 1: 
            split = message.content.split()
            location = "" 
            for i in split[1::]:
                if (split[-1] == i):
                    location += i
                else:
                    location += i + " "
            data = (get_data(location))
            current_weather = round(convert_cel(data['main']['temp']), 2)
            feels_like = round(convert_cel(data['main']['feels_like']), 2)
            country_origin = data['sys']['country']
            conditions = data['weather'][0]['main']
            humidity = data['main']['humidity']
            temp_min = round(convert_cel(data['main']['temp_min']), 2)
            temp_max = round(convert_cel(data['main']['temp_max']), 2)
            if (country_origin == "US"):
                wind_speed = str(data['wind']['speed']) + " m/h"
            else: 
                wind_speed = str(round(data['wind']['speed'] * 1.609344, 2)) + " km/h"
            current_emoji = choose_emoji(data['weather'][0]['icon'])
            flag = country_flag(data['sys']['country'])

            output = ">>> ***Current weather in:  " + flag + "  " + location.title() + ", " + country_origin + "  " + flag + "***" + "\n" + \
                    "Current weather is: **" + conditions + " " + current_emoji + "\n" + "**" \
                    "Temperature: **" + str(current_weather) + "°C " + "**" + "\n" + \
                    "Feels like: **" + str(feels_like) + "°C" + "**" + "\n" + \
                    "Humiditity: **" + str(humidity) + "%" + "**" + "\n" + \
                    "Min: **" + str(temp_min) + "°C" + "**" + "\n" + \
                    "Max: **" + str(temp_max) + "°C" + "**" + "\n" + \
                    "Wind speed: **" + wind_speed + "**" + "\n"
            await message.channel.send(output)






    except KeyError: 
        await message.channel.send("> City not found, try again")




# add local functionality 
# add the day 


client.run(TOKEN)