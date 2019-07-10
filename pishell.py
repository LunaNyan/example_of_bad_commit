#!/usr/bin/python3
import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print('name : ' + client.user.name)
    print('id   : ' + client.user.id)
    await client.change_presence(game=discord.Game(name=str(os.popen('uptime').read())))

@client.event
async def on_message(message):
    if str(message.channel.id) == 'specific channel id' and message.author.id == 'your account id':
        try:
            await client.send_message(message.channel, str(os.popen(shl_str).read()))
        except:
            await client.send_message(message.channel, ':facepalm:')

client.run('bot token')
