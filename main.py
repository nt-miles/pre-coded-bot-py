import discord
import json
import os
import aiohttp
import asyncio
import random
import re
from setuptools import setup
from discord.ext import commands

#initial_extensions = ['Main',
#                      'Fun',
#                      'Info']

client = commands.Bot(command_prefix=',')


#if __name__ == '__main__':
#    for extension in initial_extensions:
#        client.load_extension(extension)

async def change_playing():
    while True:

        
        await client.change_presence(activity=discord.Game(name='Mil- wait.'))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(name='Str- wait.'))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(name='Ne- wait.'))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(name='Pre-coded by WildcatNT'))
        await asyncio.sleep(5)



@client.event
async def on_ready():
    print(f'\n\nLogged in as: {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\n')
    await client.loop.create_task(change_playing())




#    await asyncio.sleep(5)
#    await client.change_presence(activity=discord.Game(name=''))


@client.event
async def on_message(message):


    if message.author.id == client.user.id:
        return

    if '<:MSBear:666128276061945909>' in message.content:
        await message.channel.send('<a:Win95ANI:666134250306928680> Dedicated to all the hard-working people of the WCNTVerse/WildcatNT: The RPG/山猫NT: そのRPG Product Team!')


    await client.process_commands(message)

@client.command(aliases=['pingpong'])
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['h', '?'])
async def help(ctx):
 #   36393F
    helpE = discord.Embed()
 #   helpE.color()
    helpE.add_field(name="BASIC:", value="`,help` `,ping`")
    msg = await ctx.send('Grabbing the commands, please wait!')
    await asyncio.sleep(3.0)
    await msg.edit(content='here ya go!')
    await msg.edit(embed=helpE)



client.run('token_here')
