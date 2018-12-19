import discord
import argparse
from amzsear import AmzSear
import asyncio
import re
from args import ArgumentParser
from time import sleep

client = discord.Client()
monitors = []
checkings = []
token = open('token.key', 'r')
token = token.read()

url_reg=r"(?i)amazon\.(ca|com|jp|au|uk|br|de|es|fr|in|it|mx|nl|sg)/([^\s]+)"

#search parse
search_parse = argparse.ArgumentParser()
search_parse.add_argument('--region', '-r', help='choose for regions \n |AU| Australia |\n |BR| Brazil    |\n |CA| Canada    |\n |CN| China     |\n |De| Germany   |\n |ES| Spain     |\n |FR| France    |\n |IN| India     |\n |IT| Italy     |\n |JP| Japan     |\n |MX| Mexico    |\n |NL| Holland   |\n |SG| Singapore |\n |UK| England   |\n |US| America   |\n')

#url parse setup
url_parse = ArgumentParser(prog="!addurl")
url_parse.add_argument('url')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, '''```!help - displays this message \n!addurl - watches the url given \n!add - watches the first amazon item it finds \n!search - searches the first page \n \n \nfor more information type in any command and then --help for example: !add --help```''')
    
    if message.content.startswith('!addurl'):
        try:
            url_parse.parse_args(message.content[7:].split())
        except argparse.ArgumentError or exc:
            client.send_message(message.channel,'''```{}```'''.format(exc.message, '\n', exc.argument))


client.run(token)
token.close()
