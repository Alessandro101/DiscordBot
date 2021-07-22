import discord
#pip install PyNaCl
import random
from discord.ext import commands

token = 'ODU4MTcyMTQ0ODQzNzUxNDM0.YNaRFw.nuwmsO7zMGS0cKAPWLeFzeDDE2E'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print("I'm up to snuff, and gots me an ace machine!")

@client.event
async def on_message(message):
  channel = client.get_channel(856928296280129587) 
  generic_garbage = ["ask","gamepass","xqc","a.s.k","crazy","asq","bean"]
  greetings = ["hi","hey","greetings","bonjour"]
  voice_state = message.author.voice
  for i in range(len(generic_garbage)):
    if generic_garbage[i] in message.content.lower():
      if voice_state is None:
            await message.channel.send('I\'ll get you next time, varmint')  
      else:
            await message.channel.send("I\'m on it, Blackshoe!")
            channel = client.get_channel(856928296280129587) 
              # channel now holds the channel you want to move people into

            member = message.author
              #member now holds the user that you want to move
            await member.move_to(channel)
  for i in range(len(greetings)):
    if greetings[i] + " corki" in message.content.lower():
      await message.channel.send("Howdy!")
  if "sus" in message.content.lower():
    await message.channel.send("AMOLJUSS!?")
  if "fuck you" in message.content.lower() or "fuck corki" in message.content.lower():
    await message.channel.send("Let's just say, yer an india delta india oscar tango")
  if message.author.id == 310875859630292994:
              await member.move_to(channel)




  await client.process_commands(message)


@client.command()
async def lines(ctx):
    corki_lines = ["That just goes to show you yer nothin\' but a whiskey delta","Speed of heat!","Another fine sortie!","This is Major Tom to ground control!","Zoooom...!","Lima Oscar Lima","It\'s a Charlie Foxtrot","Consider yourself spanked, nugget!"]
    num = random.randint(0,len(corki_lines)-1)
    await ctx.send(corki_lines[num])

@client.command()
async def laugh(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = discord.FFmpegPCMAudio('Corki Laugh 10 Minutes.mp3')
    player = await voice.play(source)

  else:
    await ctx.send("Yer not in a call, whipper snapper")

@client.command()
async def leave(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.disconnect()

  else:
    await ctx.send("Yer not in a call, whipper snapper")


client.run(token)