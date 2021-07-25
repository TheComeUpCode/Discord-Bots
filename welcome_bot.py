import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import re
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('DISCORD_TOKEN')
INTRO_ID = os.getenv('INTRO_ID') 
RULES_ID = os.getenv('RULES_ID') 

MESSAGE = ("Hey {name}! Welcome To Bukola's Discord Channel!" 
"We are so happy to have you here :)"
"Please introduce yourself here <#{intro_server}> & "
"Don't for check out the rules of this server <#{rules_server}>"
.format(name="",intro_server=INTRO_ID,rules_server=RULES_ID))

# enable privileged intent
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

# prep client
client = discord.Client(command_prefix=',', intents=intents)
@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))

# send private message to new members
@client.event
async def on_member_join(member):
    logging.info('A New Member Just Joined')
    # sending the messag to usser
    await member.send(MESSAGE.format(member.name))
    # send them a welcome message 


client.run(TOKEN)