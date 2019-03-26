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
status = ['SnorWare V1.0', 'Gemaakt door Peter R. de Vries#2938', 'DM mij als je een bot wilt', 'Laatste onderhoud: 19:47 25-2-2019', 'Inviten? Stuur Peter R. de Vries#2938 een dm!', 'Ik rook wiet als peter r de vries...', 'gebruik eens !fnloc of !jn :D', 'Nieuws: De bot is nu 100% nederlands. :D (Idee: @matthijs0409)']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(7)


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='SnorWare Update... (over enkele seconden is er een nieuwe versie!)', type = 2))
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
    if message.content.startswith('!ks'):
        await client.send_message(message.channel, "Je hebt suicide gekermit :D (probeer het eens samen met Kermit!)")
    if message.content.startswith('!up35534535352345'):
        await client.send_message(message.channel, "DE V1.0 UPDATE IS ONLINE! EINDELIJK IS DE BOT UIT DE BETA TEST. :D WIJ WENSEN U VEEL PLEZIER MET ONZE BOT. :D")
    if message.content.startswith('!fijne dag'):
        await client.send_message(message.channel, "Dankuwel! Namens Peter R de vries ook een fijne dag!") 
    if message.content.startswith('warn'):
        await client.send_message(message.channel,'Alright, Succesfully warned!')
    if(message.channel.id == "5345353455345345"):
        await client.add_reaction(message, ":Safe:546989214932140032")
    if message.content == 'help':
        em = discord.Embed(description='Commands: !fnloc !jn, !km, !vriend, !8ball, !wiet, !wd, !gevaarlijk')
        em.set_image(url='https://discordapp.com/assets/ba74954dde74ff40a32ff58069e78c36.png')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('!jn'):
        randomlist = ['Ja','Nee']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!wd'):
        randomlist = ['Eten','Vieze dingen kijken','Youtube kijken','winkelen','gamen','slapen','Privé dingen','afspreken','Suicide Kermitten']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!fnloc'):
        randomlist = ['Junk Junction','Lazy links','the block','haunted hills','pleasant park','loot lake','tomato temple','wailing woods','snobby shores','tilted towers','dusty divot','retail row','lonely lodge','shifty shafts','salty springs','frosty','polar','fatal fields','paradise palms','happy hamlet','lucky landing']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!km'):
        randomlist = ['kop','munt']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!vriend'):
        randomlist = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!hoelang'):
        randomlist = ['1 minuut','15 minuten','1 uur','2 uur','5 uur','10 uur','12 uur','23 uur en 59 minuten','30 seconden','45 minuten']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!8ball'):
        randomlist = ['Ja','Nee','sure','Nope','wtf','WAHAHA NOPE']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!gevaarlijk'):
        randomlist = ['Yes','No']
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
        em = discord.Embed(description='hier heb je een foto van een guy met een youtube kanaal. hij is erg gay en heeft een dakreparatie bedrijf...')
        em.set_image(url='https://www.dgvservices.nl/wp-content/uploads/2015/08/Logo-DGV.png')
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
        await client.send_message(message.channel,'Ik draai op dit moment op SnorWare V0.9.1.1                                                                                                                                                 Bijna V1.0!')
    if message.content.upper() == 'WTF':
        await client.send_message(message.channel,'let op je taal!')
    if message.content.upper() == 'PAGA':
        await client.send_message(message.channel,'let op je taal!')
    if message.content.upper() == 'PAGGS':
        await client.send_message(message.channel,'let op je taal!')
    if message.content.upper() == 'TYFUS':
        await client.send_message(message.channel,'let op je taal!')
    if message.content.upper() == 'PING':
        await client.send_message(message.channel,'let op je taal!')
    if message.content.upper() == 'KKR':
        await client.send_message(message.channel,'let op je taal!')
    if message.content.upper() == 'KANKER':
        await client.send_message(message.channel,'let op je taal!')
    if ('WTF') in message.content.upper():
       await client.delete_message(message)
    if ('KUT') in message.content.upper():
       await client.delete_message(message)
    if ('PAGGA') in message.content.upper():
       await client.delete_message(message)
    if ('TYFUS') in message.content.upper():
       await client.delete_message(message)
    if ('!up35534535352345') in message.content.upper():
       await client.delete_message(message)
    if ('KKR') in message.content.upper():
       await client.delete_message(message)
    if ('KANKER') in message.content.upper():
       await client.delete_message(message)
    if message.content.upper().startswith('!SAY'):
        if "547024431504162839" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Rozen zijn rood, Matthijs is een schaap (vreemd wezen) jij hebt geen toegang tot dit command. (vraag toegang aan demanmetsnor112)")
client.loop.create_task(change_status())
client.run('NTM5NTA1NDgwMTk2OTQ3OTg4.DzDVoQ.5qLPGFkyNJQb4mJSqz-TEAy1h_0')
