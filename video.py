import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
from itertools import cycle


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
status = ['SnorWare V0.6', 'Gemaakt door Peter R. de Vries#2938', 'DM mij als je een bot wilt', 'Laatste onderhoud: 14:47 18-2-2019', 'Inviten? Stuur Peter R. de Vries#2938 een dm!', 'Ik rook wiet als peter r de vries...', 'checking for updates..', 'No update found.']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(10)


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='SnorWare V0.5', type = 2))
    print('snorbot is ready :)')
    
@client.event
async def on_member_join(member):
    await client.send_message(member, "Welkom bij VDV! Heb een leuke tijd en vergeet zeker niet om een command zoals !yesno te proberen of natuurlijk 'help' fijne dag!")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "Ik ben gemaakt door Peter R de vries (voor als je ook een bot wilt)")
    await client.send_message(member, "Je kan Peter R de vries ook inhuren als developer! (roblox)")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "Je kan altijd een applicatie doen met -new (in bot commmands)")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "Question: Mag ik een developer zoals peter r de vries een bericht zenden? A: Ja tuurlijk! (Peter reageert redelijk snel)")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "Question: Waarom krijg ik dit bericht? A: Ugh, Ga hersenen kweken ofzo -_-")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "Question: Mag ik wiet roken in jullie server? A: (!wiet) Ja tuurlijk!! (samen met peter R. de vries xD)")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "BELANGRIJK: Question: Wat moet ik doen als jullie bot offline is? A: 1.Koop een JBL boombox 2.Download TTS 3. voer in: ALARM ALARMM SNORWARE.EXE IS OFFLINEEEEEEE HELPPPPPPPP DE WERELD GAAT TEN EINDE AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH 3.klik op Play 4.Ren door je straat (indien mogelijk door de hele wereld) met je speaker en zet het volume op 100 (indien mogelijk 200)")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "Bedankt voor het lezen en heb een fijne dag! (!fijne dag)")

@client.event
async def on_message(message):
    if message.content.startswith('!wiet'):
        await client.send_message(message.channel, "Je hebt wiet gerookt! :D (probeer het eens met peter R de vries)")
    if message.content.startswith('!fijne dag'):
        await client.send_message(message.channel, "Dankuwel! Namens Peter R de vries ook een fijne dag!") 
    if message.content.startswith('warn'):
        await client.send_message(message.channel,'Alright, Succesfully warned!')
    if(message.channel.id == "491253757141581825"):
        await client.add_reaction(message, ":Safe:546989214932140032")
    if message.content == 'help':
        em = discord.Embed(description='Commands: !fnloc !yesno, !coinflip, !friend, !8ball, !wiet')
        em.set_image(url='https://discordapp.com/assets/ba74954dde74ff40a32ff58069e78c36.png')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('!yesno'):
        randomlist = ['Yes','No']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!fnloc'):
        randomlist = ['Junk Junction','Lazy links','the block','haunted hills','pleasant park','loot lake','tomato temple','wailing woods','snobby shores','tilted towers','dusty divot','retail row','lonely lodge','shifty shafts','salty springs','frosty','polar','fatal fields','paradise palms','happy hamlet','lucky landing']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!coinflip'):
        randomlist = ['head','coin']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!friend'):
        randomlist = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!8ball'):
        randomlist = ['Yes','No','sure','Nope','wtf','WAHAHA NOPE']
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
        em = discord.Embed(description='hier heb je een foto van een skipper... hij is erg gay')
        em.set_image(url='https://media.discordapp.net/attachments/491228753268310018/539507547569258496/865db2d7-cddc-4ab2-8f29-e41fe87b74d3-1526542591593.png?width=968&height=403')
        await client.send_message(message.channel, embed=em)
    if message.content == 'pls 4k':
        em = discord.Embed(description='Je hebt geen toegang tot deze command. De fbi is onderweg...')
        em.set_image(url='https://memegenerator.net/img/images/72477136.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'Pls 4k':
        em = discord.Embed(description='Je hebt geen toegang tot deze command. De fbi is onderweg...')
        em.set_image(url='https://memegenerator.net/img/images/72477136.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == 'ever1':
        await client.send_message(message.channel,'@everyone 1')
    if ('ever1') in message.content:
       await client.delete_message(message)
    if ('@everyone 1') in message.content:
       await client.delete_message(message)
    if message.content == 'ever1 matt':
        await client.send_message(message.channel,'Deze command is buiten gebruik.')
    if message.content == 'ever1 storm':
        await client.send_message(message.channel,'Deze command is buiten gebruik.')
    if message.content == 'ever1 yan':
        await client.send_message(message.channel,'Deze command is buiten gebruik.')
    if ('ever1 matt') in message.content:
       await client.delete_message(message)     
    if ('ever1 storm') in message.content:
       await client.delete_message(message)  
    if ('ever1 yan') in message.content:
       await client.delete_message(message)
    if message.content == 'v':
        await client.send_message(message.channel,'Ik draai op dit moment op SnorWare V0.6')
    if message.content == 'wtf':
        await client.send_message(message.channel,'let op je taal!')
    if message.content == 'KKR':
        await client.send_message(message.channel,'let op je taal!')
    if message.content == 'kkr':
        await client.send_message(message.channel,'let op je taal!')
    if message.content == 'ping':
        await client.send_message(message.channel,'let op je taal!')
    if message.content == 'PING':
        await client.send_message(message.channel,'let op je taal!')
    if message.content == 'kanker':
        await client.send_message(message.channel,'let op je taal!')
    if message.content == 'KANKER':
        await client.send_message(message.channel,'let op je taal!')
    if ('wtf') in message.content.upper():
       await client.delete_message(message)
    if ('kut') in message.content:
       await client.delete_message(message)
    if ('kud') in message.content:
       await client.delete_message(message)
    if ('ping') in message.content:
       await client.delete_message(message)
    if ('PING') in message.content:
       await client.delete_message(message)
    if ('kanker') in message.content:
       await client.delete_message(message)
    if ('KANKER') in message.content:
       await client.delete_message(message)
    if message.content.upper().startswith('!SAY'):
        if "547024431504162839" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Rozen zijn rood, Matthijs is een schaap (vreemd wezen) jij hebt geen toegang tot dit command. (vraag toegang aan demanmetsnor112)")
client.loop.create_task(change_status())
client.run('NTM5NTA1NDgwMTk2OTQ3OTg4.DzDVoQ.5qLPGFkyNJQb4mJSqz-TEAy1h_0')
