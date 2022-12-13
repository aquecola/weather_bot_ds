from logging import exception
import nextcord
from nextcord.ext import commands
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.slash_command(description="Узнайте погоду вашего мухосранска")
async def weather(interaction: nextcord.Interaction, where):
    owm = OWM(os.environ.get('TOKEN2'))
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(where)
    where = observation.weather
    temp = int(where.temperature('celsius')['temp'])
    speed = where.wind()['speed']
    humidity = where.humidity

    try:
        await interaction.response.send_message(f"```Температура: {temp}℃ | Скорость ветра: {speed} м/с | Влажность: {humidity}%```")
    except exception:
        await interaction.response.send_message(f"Ты дурик")




bot.run(os.environ.get('TOKEN'))