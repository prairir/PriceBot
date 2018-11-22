import discord
import asyncio
import re
from time import sleep

client = discord.Client()
monitors = []
checkings = []
token = open('token.txt', 'r')
token = token.read()

url_reg=r"(?i)amazon\.(ca|com|jp|au|uk|br|de|es|fr|in|it|mx|nl|sg)/([^\s]+)"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, '''```!help - displays this message \n!addurl - watches the url given \n!add - watches the first amazon item it finds \n!search - searches 10 items```''')
    
    if message.content.startswith('!addurl'):
        url = message.split()[1]

client.run(token)
token.close()
