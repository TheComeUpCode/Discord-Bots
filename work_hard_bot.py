
import os, re, logging
from dotenv import load_dotenv

import discord

load_dotenv()
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    logging.info('We have logged in as {0.user}'.format(client))


"""Listen For Work Hard In Message and Respond With Nap Hard"""
@client.event
async def on_message(message):
    logging.info('WE GOT A MESSAGE')
    pattern_re = re.compile(r"work hard", re.IGNORECASE)
    if re.search(pattern_re, message.content): 
        await message.channel.send('Dont Forget To Nap Hard Too!')

client.run(TOKEN)