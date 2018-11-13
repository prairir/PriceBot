import discord
from PriceBot import listings
from time import sleep

client = discord.Client()
monitors = []
checkings = []


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    print("hello")
