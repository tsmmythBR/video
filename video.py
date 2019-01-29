import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='SnorWare V0.22', type = 2))
    print('snorbot is ready :)')


@client.event
async def on_message(message):
    if message.content.startswith('!friend'):
        randomlist = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!8ball'):
        randomlist = ['Ja','Nee','Zeker','Nope','wtf','WAHAHA NOPE']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == 'snor':
        em = discord.Embed(description='hier heb je een foto van een snor :)')
        em.set_image(url='https://cdn-images-1.medium.com/max/1440/1*lH3QlW2O3G5A_pAhhJU0Dw.jpeg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'matthijs':
        em = discord.Embed(description='hier heb je een foto van een vreemd wezen...')
        em.set_image(url='https://cdn.discordapp.com/attachments/491228753268310018/539507413766635521/schaap.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'yannick':
        em = discord.Embed(description='hier heb je een foto van een skipper...')
        em.set_image(url='https://media.discordapp.net/attachments/491228753268310018/539507547569258496/865db2d7-cddc-4ab2-8f29-e41fe87b74d3-1526542591593.png?width=968&height=403')
        await client.send_message(message.channel, embed=em)
    if message.content == 'ever1':
        await client.send_message(message.channel,'@everyone 1')
    if message.content == 'gozer':
        await client.send_message(message.channel,'G*st, Stop met het g woord. Demanmetsnor112 wordt er bang van!')
    if message.content == 'Gozer':
        await client.send_message(message.channel,'G*st, Stop met het g woord. Demanmetsnor112 wordt er bang van!')
    if message.content == '@Matthijs0409':
        await client.send_message(message.channel,'vieze nazi, ga snor niet taggen')
    if ('gozer') in message.content:
       await client.delete_message(message)
    if ('Gozer') in message.content:
       await client.delete_message(message)
    if ('Gast') in message.content:
       await client.delete_message(message)
    if ('gast') in message.content:
       await client.delete_message(message)
    if ('ever1') in message.content:
       await client.delete_message(message)
    if ('@everyone 1') in message.content:
       await client.delete_message(message)
client.run('NTM5NTA1NDgwMTk2OTQ3OTg4.DzDVoQ.5qLPGFkyNJQb4mJSqz-TEAy1h_0')
