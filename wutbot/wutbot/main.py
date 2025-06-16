import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
import asyncio
import random
from replit import db
from bs4 import BeautifulSoup
import youtube_dl
import requests
import inspect
import jaro  # pip install jaro-winkler
# put this bit in your oninit

import sys
print(sys.version)



charnames: set
#  charnames needs to be available to the function


class Character:

    def __init__(self):
        self.hull = ""
        self.skills = []
        self.stats = []
        self.weapons = []
        self.fleetTech = []
        self.barrages = []

    def __str__(self):
        retval = ""
        for i in range(len(self.stats[0])):
            retval += f"{self.stats[0][i]}: {self.stats[1][i]} | "
        retval = retval.strip(" | ") + "\n"
        for i in range(len(self.weapons)):
            if i < 3:
                item = self.weapons[i]
                retval += f"slot {item[0]}, {item[3].split('→')[-1].strip(' ')} {item[2]} @{item[1].split('→')[-1]}\n"
            else:
                retval += f"Equipable augments: {''.join(self.weapons[i][2])}\n"
        retval += "%$#"
        for i in range(len(self.skills)):
            retval += f"-{self.skills[i][0]}: {self.skills[i][1]}\n\n"
        for i in range(len(self.fleetTech)):
            retval += f"{['On collection:', 'On 120:'][i]} {' '.join(self.fleetTech[i][0])} get +{self.fleetTech[i][2]} {self.fleetTech[i][1]}\n"
        retval += "%$#" + '%$#'.join([str(x) for x in self.barrages])
        return retval

db['count']
db['stuff'] 
db['wutwallet']
db['eve']

client = commands.Bot(command_prefix="", case_insensitive=True, help_command = None)
emojis = ["<:wut:839980374724968448>"]


@client.event
async def on_ready(): 
  page = requests.get("https://azurlane.koumakan.jp/wiki/List_of_Ships")
  soup = BeautifulSoup(page.content, "html.parser")
  names = []
  for table in soup.findAll("table")[0:4]:
    for row in table.find("tbody").findAll("tr"):
        data = row.findAll("td")
        if len(data) == 11:
            names.append(str(data[1].text))
  global charnames
  charnames = set(names)
  
  for emoji in client.emojis:
      emojis.append(emoji)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="tranqgaming"))
  


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
        msg = '**Still On Cooldown** Stop Killing Wut Bot <:konatacri:791902291933659166>. Please Try Again In {:.2f} seconds'.format(error.retry_after)
        await ctx.send (msg, delete_after=error.retry_after)


@client.listen('on_message') 
async def stuff(message):
  if not message.author.bot:
    if "tranq" in message.clean_content.lower():
            if (not message.content.lower().startswith('tranqcount')):
              if (not message.content.lower().startswith('tranqreset')):
                count = db['count']
                count += 1
                db['count'] = count
                emoji = client.get_emoji(937866192583016559)
                await message.add_reaction('👀')
    if "bip" in message.clean_content.lower():
                await message.add_reaction('👣')
                await message.add_reaction('🦶')
                await message.add_reaction('🐾')

    a = random.randint(1,1000)
    if (a == 69):
        b = random.randint(1,len(emojis) - 1)
        await message.add_reaction(emojis[b])

              






@client.command()
async def tranqcount(ctx):
      count = db['count']
      await ctx.channel.send(str(count)+" tranqs spotted") 
    
    
@client.command()
@commands.has_permissions(administrator=True)
async def tranqreset(ctx):
    db['count']=0
    await ctx.channel.send("Oops I forgot how many tranqs there were. Let's restart!")




@client.command()
async def put(ctx, a:int):
    put = db['stuff']
    put += a
    db['stuff'] = put
    await ctx.channel.send(str(put)+" in the pot") 

@client.command()
async def take(ctx, a:int):
    put = db['stuff']
    put -= a
    db['stuff'] = put
    await ctx.channel.send(str(put)+" in the pot") 


@client.command()
async def wutwalletreset(ctx):
@commands.has_permissions(administrator=True)
    db['wutwallet']=1000
    await ctx.channel.send("I just got a cash injection <:nicodab:838233787535851550>")

@client.command()
async def wutwallet(ctx):
      wallet = db['wutwallet']
      await ctx.channel.send("I have "+str(wallet)+" WutBucks") 

@client.command()
async def wutplayblackjack(ctx):
  await ctx.channel.send("Dealing...")

  def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["e", "E", "c", "C"]

    
  cards = ['Ace', 'Two', "Three", 'Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
  value=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  x = random.randint(0,12)
  y = random.randint(0,12)
  h = ""
  msg = " "
  ala = random.randint(50, 100)
  
  hand = [cards[x], cards[y]]
  handr = [x, y]
  handv = [value[x], value[y]]
  cpu = random.randint(17,24)
  await ctx.channel.send("Your current cards: "+hand[0]+", "+hand[1])
  
  while sum(handv)<22:
    await ctx.channel.send('Press E to end, Press C to continue')
    msg = await client.wait_for("message", check=check)
    
    if msg.content == "e":
      break
    if msg.content== "E":
      break
      
    z = random.randint(0,13)
    hand.append(cards[z])
    handr.append(z)
    handv.append(value[z])
    h="New Hand: "
    for g in hand:
      h+=g+", "
    await ctx.channel.send(h)
    if (sum(handv)>21):
      value[0] = 1

    handv = []
    for x in handr:
      handv.append(value[x])
    
      
      
      
    
  await ctx.channel.send("Wutbot had "+str(cpu)+". You had "+str(sum(handv))+".")
  wallet = db['wutwallet']
  if sum(handv)>21 and cpu>21:
    await ctx.channel.send('Tie! <:wutblind:860554148311334914>')
  elif sum(handv)>21:
    wallet+=ala
    db['wutwallet']=wallet
    await ctx.channel.send('You Lose! <:wut69:864546752665223188>')
    await ctx.channel.send('Wut stole '+str(ala)+' WutBucks from you! Wut now has '+str(wallet)+' WutBucks')
  elif cpu>21:
    wallet-=ala
    db['wutwallet']=wallet
    await ctx.channel.send('You Win! <:nicodab:838233787535851550>')
    await ctx.channel.send('You stole '+str(ala)+' WutBucks from Wut! Wut now has '+str(wallet)+' WutBucks')
  elif sum(handv)>cpu:
    wallet-=ala
    db['wutwallet']=wallet
    await ctx.channel.send("You Win! <:nicodab:838233787535851550>")
    await ctx.channel.send('You stole '+str(ala)+' WutBucks from Wut! Wut now has '+str(wallet)+' WutBucks')
  elif sum(handv)<cpu:
    wallet+=ala
    db['wutwallet']=wallet
    await ctx.channel.send('You Lose! <:wut69:864546752665223188>')
    await ctx.channel.send('Wut stole '+str(ala)+' WutBucks from you! Wut now has '+str(wallet)+' WutBucks')
  else:
    await ctx.channel.send('Tie! <:wutblind:860554148311334914>')
    
      
    
  

#single commands

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def wutping(ctx):
    if round(client.latency * 1000) <= 50:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0xffd000)
    elif round(client.latency * 1000) <= 200:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0xff6600)
    else:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0x990000)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def wut(ctx):
        await ctx.channel.send ('<:wut69:864546752665223188>')

@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def wutkill(ctx,*, msg):
        await ctx.channel.send('<:wut:839980374724968448><:gunr:1007007330807857175>' + msg)
       

@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def cherino(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/901589065747546153/unknown.png')

@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def wutfeed(ctx):
        await ctx.channel.send('<:wut:839980374724968448><:donut:887472421983101009>')

@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def wutpet(ctx):
  await ctx.channel.send('<a:wutpet:916337047176888320>')

@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def ryuusei(ctx):  
        await ctx.channel.send('<:ryuusei:864547515227832352>')



@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def craig(ctx):
        await ctx.channel.send("https://cdn.discordapp.com/attachments/749339853661011968/889220306043023381/unknown.png")

@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def jeff(ctx):
        await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/898394360792645652/unknown.png")
        
@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def hype(ctx):  
        await ctx.channel.send('<a:hype:834557242707411044>')

@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def pray(ctx):  
        await ctx.channel.send('<:htpray:834584994692202527>')

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def smug(ctx):  
        await ctx.channel.send('https://tenor.com/view/azur-lane-taihou-evil-smile-gif-20485240')

@client.command()  
@commands.cooldown(1, 1, commands.BucketType.user) 
async def essex(ctx):  
        await ctx.channel.send('<:essexkex:827622052826841128>')

@client.command()
async def wutsay(ctx,*,message):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{message}")



@client.group(invoke_without_command=True)
async def hi(ctx):
    # general functionality, help, or whatever.
    pass

@hi.command()
async def nick(ctx):
    await ctx.channel.send('https://cdn.discordapp.com/attachments/762741322167222293/1010307004952223854/unknown.png')
    pass

@client.command()  
@commands.cooldown(1, 1, commands.BucketType.user) 
async def spin(ctx):  
        await ctx.channel.send('<a:monkeyspin:835148624466935879>')

@client.command()  
@commands.cooldown(1, 1, commands.BucketType.user)
async def bonk(ctx):  
        await ctx.channel.send('<a:bonkcheshire:836724394281271326>')


@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def salad(ctx):
        await ctx.channel.send("<:saladbar:843326534726451200>")

        
@client.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def suisei(ctx):
        await ctx.channel.send("<:suisei:844972354932834315>")

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def painpeko(ctx):
        await ctx.channel.send("https://preview.redd.it/dvk3bft2a9l51.jpg?auto=webp&s=d5e53605dc0e99ed55884fc00c9b965c7dd38e7c")
        
@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def thinkmark(ctx):
        await ctx.channel.send("https://tenor.com/view/think-mark-invincible-omniman-gif-21416554")
        

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def glueman(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/845794721455800420/2Q.png')

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def woke(ctx):
        await ctx.channel.send("<a:wutwoke:851971298883928087>")

@client.command()
async def confetti(ctx):
        await ctx.channel.send("<a:weewoo:885348019615182888>")



#vc

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def wutjoin (ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
        await ctx.send("Hello!")
    else:
        voice = await channel.connect()
        await ctx.send("Hello!")
@client.command()
async def wutplay(ctx, url : str):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    song_there = os.path.isfile("song.mp3")
    voice.stop()
    if song_there:
          os.remove("song.mp3")
    await ctx.send("Loading...")


    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send("Playing...")


@client.command()
async def wutleave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("Bye!")
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def wutpause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("Paused")
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def wutresume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("Resumed")
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def wutstop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("Stopped")



#albasalute
        
@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def albasalute(ctx):
        n = random.randint(1,23)
        if (n == 1):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/749309042047844412/846170865895997460/Untitled_Artwork.png")
        if (n == 2):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/749309042047844412/846170454020718602/Untitled_Artwork.png")
        if (n == 3):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/749309042047844412/846169840226140180/Albasalute.png")
        if (n == 4):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/749309042047844412/846171733668397066/Untitled_Artwork.png")
        if (n == 5):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/749309848126226462/846956473787088906/albabruh.png")
        if (n == 6):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847123587826712586/reapor.png")
        if (n == 7):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847125116671361034/waitnogoback.png")
        if (n == 8):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847266902916071435/Albalulu.png")
        if (n == 9):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847272860510715954/Untitled_Artwork.png")
        if (n == 10):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/834199859187810308/847324794696368138/Untitled_Artwork.png")
        if (n == 11):
          await ctx.channel.send("https://tenor.com/view/spanish-no-one-expected-inquisition-gif-18096957")
        if (n == 12):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847638952521498654/albessex.png")
        if (n == 13):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847641571670753320/Untitled_Artwork.png")
        if (n == 14):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847640880885661696/Untitled_Artwork.png")
        if (n == 15):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847642541108363354/whysbacore.png")
        if (n == 16):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847645534667014144/salbarcore.png")
        if (n == 17):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847648709265326090/albaloco.png")
        if (n == 18):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/748012052588789893/847894347701420042/albipcore.png")
        if (n == 19):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/749309848126226462/852994666694049812/Untitled_Artwork.png")
        if (n == 20):
          await ctx.channel.send("https://cdn.discordapp.com/attachments/749309848126226462/852994639265923102/Untitled_Artwork.png")
        if (n == 21):
          await ctx.channel.send("https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825")
        if (n == 22):
          await ctx.channel.send("https://media.discordapp.net/attachments/748012052588789893/962013668185346098/albachecore.png")
        if (n == 23):
          await ctx.channel.send("https://media.discordapp.net/attachments/748012052588789893/962014523542339654/saladcore.png")
      




#multiple actions


@client.command()
@commands.cooldown(1, 6, commands.BucketType.user)
async def dab(ctx):  
        await ctx.channel.send('<:nicodab:838233787535851550>')
        await asyncio.sleep(0.4)
        await ctx.channel.send('<:nicodab2:842184298366107669>')
        await asyncio.sleep(0.4)
        await ctx.channel.send('<:nicodab:838233787535851550><:nicodab2:842184298366107669>')
        await asyncio.sleep(1.2)
        await ctx.channel.send ('<:nicofire:842186105469927444>')
 




#azure
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def wutazur(ctx):
        await ctx.channel.send("""**Wut Bot Quick Links for all your Azur Needs**
wutship = ship tier list
wutgear = gear recommendations
wutcat = cat skill tier list
wutsiren = opsiren stuff
wutpr = pr ship ratings
wutprbp = pr ships bp requirements
wutairstrike = airstrike reload calculator + ship acv values
wutpvp = info about pvp rankings
wutdrop = notable drop only ships
wutsos = info about sos missions
wutsub = sub aux gear info
wutmeta = information about current META ship
wutevent = current event's wiki
wutlab = research stuff
wutarchive = what to farm in war archives""")


@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutship(ctx):
        await ctx.channel.send('https://slaimuda.github.io/ectl/#/home - EN Tier List')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutgear(ctx):
        await ctx.channel.send("https://imgur.com/a/TNpH1rL - Nerezza's Guide")
        await ctx.channel.send("https://azurlane.koumakan.jp/Gear_Lab - Mats needed to craft Gear Lab gear")

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutpr(ctx):
        await ctx.channel.send('PR Ratings: ')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/865591093727199272/unknown.png')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/865591120062054480/unknown.png')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/865591133479108658/unknown.png')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/865591163314372658/unknown.png')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutprbp(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/643697081210503168/841129311683870742/BPs.jpg')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/850884708866850828/872882104608895026/unknown.png')
        await ctx.channel.send('PR1 allows the use of Coins to replace BP. Every day the first 15 purchases are discounted, this is a combined amount amongst all ships, you do not get 2 free prints per day per ship for example. This discount resets each day 4 hours after reset time.')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749309848126226462/851144904469512272/unknown.png')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutairstrike(ctx):
        await ctx.channel.send('https://thebombzen.com/azur-lane/airstrike-reload.html - Airstrike Reload Calculator')
        await ctx.channel.send('https://azurlane.koumakan.jp/List_of_Ships_by_Airspace_Control_Value - Ship ACV')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutsiren(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/834274390082191400/958960212923019304/Azur_Lane_OS_Stat_Sheet_-_v7.png')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/844811332468342784/Equipment_Guide_by_Nerezza7031_The_Fubuki_Shill_-_OpSi_Image_Guide-page-001.jpg')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/921064703604695110/unknown.png')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutcat(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/816732733803986964/unknown.png')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutpvp(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/820425639861551124/unknown.png')
        
@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutdrop(ctx):
        await ctx.channel.send("Credits to SmolSpite")
        await ctx.channel.send('https://cdn.discordapp.com/attachments/850884708866850828/1001547281532735518/unknown.png')


@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutsos(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/845788659290210364/unknown.png')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/749339853661011968/832435793837686814/Vb7jfTX.png')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutsub(ctx):
        await ctx.channel.send('https://media.discordapp.net/attachments/749339853661011968/841475191711858688/unknown.png?width=938&height=463')
        await ctx.channel.send("Use Nerezza's Guide for Torp Recs")

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutmeta(ctx):
        await ctx.channel.send('Current META Ship - Gneisenau Meta')
        await ctx.channel.send('https://docs.google.com/spreadsheets/d/1slJmgQAH5AwtotwYbJF1eiIZvPhg3Mrh/edit#gid=934314749')
        await ctx.channel.send('https://azurlane.koumakan.jp/META_Lab - Extra Stuff')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutevent(ctx):
        a = db['eve']
        await ctx.channel.send(a)

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
@commands.has_permissions(administrator=True)
async def wutupdateevent(ctx):
    a = str(ctx.message.content)
    db['eve']=a[14:]
    await ctx.channel.send('Updated !!')
        

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutlab(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/460645783021289472/857671111214759956/researches.png')
        await ctx.channel.send('https://media.discordapp.net/attachments/749339853661011968/881691883926065192/unknown.png?width=1023&height=340')

@client.command()
@commands.cooldown(1, 15, commands.BucketType.guild)
async def wutarchive(ctx):
        await ctx.channel.send('https://cdn.discordapp.com/attachments/821898541122191391/858832295305019392/unknown.png')
        await ctx.channel.send('https://cdn.discordapp.com/attachments/821898541122191391/858833307495301127/unknown.png')
        await ctx.channel.send('War Archives in a nutshell, courtesy of our resident SmolSpite')


@client.command()
async def wutwiki(ctx, term):
    print("i ran")
    term = term.strip("\n").strip(" ")
    url = r'https://azurlane.koumakan.jp/wiki/'
    possibles = {}
    for name in charnames:
        if jaro.jaro_metric(name, term) > 0.9:
            possibles[name.lower()] = name
    term = possibles[term.lower()] if term.lower() in possibles.keys() else term
    page = requests.get(url + term.replace(" ", "_"))
    soup = BeautifulSoup(page.content, "html.parser")
    char = Character()
    if True:
        char.hull = soup.find("div", class_="card-info").find("tbody").findAll("tr")[2].find("img", alt=True)["alt"].split("(")[1][:-1]
        [char.skills.append([x[1].text.split("CN:")[0], x[2].text.strip("\xa0\n")]) for x in [x for x in [x.findAll("td") for x in soup.find("table", class_="ship-skills wikitable").find("tbody").findAll("tr")] if len(x) == 3]]
        stats = soup.find("table", class_="ship-stats wikitable").find("tbody").findAll("tr")
        char.stats = [
            [(x.find("img", alt=True)["alt"] if x.text != "Spd" else x.text) for x in stats[0].findAll("th") if x is not None and       ((x.find("img", alt=True) and x.find("img", alt=True)["alt"] != "Anti-submarine warfare (ASW)") or x.text == "Spd")],
            [x.text for x in stats[1].findAll("td") if not (x.find("b"))]
        ]
        char.weapons = [x for x in [gear.text.strip("\n").split("\n\n") for gear in soup.find("table", class_="ship-equipment wikitable").find("tbody").findAll("tr")[2:6]]]
        techs = soup.find("table", class_="ship-fleettech wikitable").find("tbody").findAll("tr")
        for i in range(1, 4, 2):
            linetech = techs[i].findAll("td")[0]
            char.fleetTech.append([[x["title"].split("(")[1].strip(")") for x in linetech.findAll("a", title=True)], linetech.find("img", title=True)["title"], int(linetech.text)])
        soup = BeautifulSoup(requests.get("https://azurlane.koumakan.jp/wiki/User:Riceist/BarrageDatamine").content, "html.parser").findAll("table")
        tablesToSearch = [1, 13]
        n = "\n"
        for i, table in enumerate(soup): # have to search 1, and -1
            if char.hull in table.find_previous().attrs["id"]:
                tablesToSearch.append(i)
                print(i)
        for tableIndex in tablesToSearch:
            rows = soup[tableIndex].findAll("tr")[1::]
            for row in rows:
                if term.lower() in row.find("td").text.lower():
                    while True:
                      try:
                        data = row.findAll("td")
                        if data[1].text:
                            char.barrages.append(
                                f"Skill: {data[1].text}, skill Id#{data[2].text}"
                            )
                        char.barrages[-1] += f"\n=weapon Id#{data[3].text}, {data[16].text} bulllets with bullet Id#{data[4].text}, raw damage: {data[5].text}, ammo type: {data[6].text}, coefficient: {data[7].text}, {data[8].text} coeff of {data[9].text}, armor mods {data[10].text}/{data[11].text}/{data[12].text}, total damage against armor {data[17].text}/{data[18].text}/{data[19].text.strip(n)}, " + (f" {data[14].text}% chance to proc buff buffId#{data[15].text}, " if data[14].text else "") + (f" riceist notes: '{data[13].text}'" if data[13].text else "")


                        row = row.find_next_sibling()
                        if len(row) == 2 or (not row.findAll("td")[16].text):
                            break
                      except TypeError as e:
                          break # just pray that its the end of the table lol

        for val in (str(char).split("%$#")):
            if val:
              await ctx.channel.send(val)
    else:
      #except Exception as e:
        print(e)
        possibles = []
        for name in charnames:
          if jaro.jaro_metric(name, term) > 0.7:
            possibles.append(name)
        print(term + f" does not exist on the wiki did you mean one of these?\n{' '.join(possibles)}")
        await ctx.channel.send(term + f" does not exist on the wiki did you mean one of these?(capitalization matters)\n{', '.join(possibles)}")
     
        
#big math

        
        

        
    

#idk

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def wutpurge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        msg = 'Cleared by {}'.format(ctx.author.mention)
        await ctx.send (msg, delete_after=5)

@wutpurge.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Cringe Dayo")
        

    


#salad




keep_alive()
client.run(os.getenv('TOKEN'))
