import os 
import discord
from weather_data import *

TOKEN = 'NzEwNjQ4OTEzNjI2OTIzMTUz.Xr3hjw.YxSHQOQxn4pRGGjvPrn3e8K9Z1E'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('!weather'):
        await message.channel.send("Invalid, use it in the format !weather <city>")
    
    if len(message.content.split()) == 2: 
        split = message.content.split()
        data = (make_url(split[1]))
        current_weather = round(convert_cel(data['main']['temp']), 2)
        feels_like = round(convert_cel(data['main']['feels_like']), 2)
        country_origin = data['sys']['country']
        conditions = data['weather'][0]['main']
        humidity = data['main']['humidity']
        temp_min = round(convert_cel(data['main']['temp_min']), 2)
        temp_max = round(convert_cel(data['main']['temp_max']), 2)
        print(country_origin)

        output = "***Current weather in " + split[1] + ", " + country_origin + "***" + "\n" + \
                "Current weather is: " + conditions + "\n" + \
                "Temperature: " + str(current_weather) + "C! :sunny: " + "\n" + \
                "Feels like: " + str(feels_like) + "C!" + "\n" + \
                "Humiditity: " + str(humidity) + "%" + "\n" + \
                "Min: " + str(temp_min) + "C!" + "\n" + \
                "Max: " + str(temp_max) + "C!" + "\n"
        await message.channel.send(output)
        
        
    
    # add imperial detection based on country


# make an extension to get local weather 
# but also to put in a city 

client.run(TOKEN)