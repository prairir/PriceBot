import discord
from listings import Monitor


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
    if message.content.startswith('!add'):
        monitors.append(Monitor(message.author, message.content[5:]))
        print('------')
        print(len(monitors))
        monitors[len(monitors) - 1].printMon()

    if message.content.startswith('!rid'):
        b = 'a'

        for i in range(len(monitors)):
            checkings.append(monitors[i].getUrl())

        for i in range(len(checkings) - 1):
            if message.content[4:].strip() == checkings[i].strip():
                b = False
                del checkings[i]
                break

            else:
                b = True
                continue

        if b is True:
            print("url not found")

    if message.content.startswith('!print'):
        for i in range(len(monitors) - 1):
            monitors[i].printMon()

client.run('MjUxMzUzNDcxNjYyNDI0MDY0.CxiMjw.tfKoukCvYchdVSLwMp4wLb60UoY')

