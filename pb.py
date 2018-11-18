import discord
import asyncio
from time import sleep

client = discord.Client()
monitors = []
checkings = []
token = open('token.txt', 'r')
token = token.read()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, '''```!help - displays this message \n!addurl - watches the url given \n!add - watches the first amazon item \n!search - searches 10 items```''')


client.run(token)
token.close()
