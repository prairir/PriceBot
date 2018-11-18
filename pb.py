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
    print("hello")

client.run(token)
token.close()
