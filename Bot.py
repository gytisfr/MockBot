#MockBot by ~ Gytis5089

import discord
import asyncio
import random
from discord.ext.commands import Context
from discord.ext import commands

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Drive-In"))
    print('MockBot now online.')
    print(f'We are running with {round(client.latency * 100)}ms ping.')

@client.event
async def on_message(msg):
    if msg.channel.id == 960212451771699230:
        if msg.author.id != 922100799138574367:
            replything = '"'
            for el in msg.content:
                selection = random.randint(1, 2)
                if selection == 1:
                    replything = f"{replything}{el.upper()}"
                else:
                    replything = f"{replything}{el.lower()}"
            replything = f'{replything}"'
            await msg.reply(replything)

client.run('OTIyMTAwNzk5MTM4NTc0MzY3.Yb8jSg.yxPWpZCe5Wf59zZB23A8WKfSgow')