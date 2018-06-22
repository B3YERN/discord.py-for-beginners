

'''Activity is a status for your bot like Playing,Streaming,Listening and Watching Status'''

'''Okay so there's a difference between on_ready and commands using Activity'''

'''You can use on_ready event like this'''

import discord
from discord.ext import commands

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="whatever"))
  
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name="whatever", url="https://www.twitch.tv/discordapp"))
  
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="whatever"))
  
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="whatever"))
  
  
  '''If you want to use it as commands instead of on_ready event or you can also use it as commands'''
  
  
@bot.command()
@commands.is_owner()
async def play(ctx, *, game :str):
    """Playing status for the bot {Bot-Owner Only}."""
    print(*game)
    await bot.change_presence(activity=discord.Game(name="whatever"))
  
@bot.command()
@commands.is_owner()
async def stream(ctx, *, title : str):
    """Streaming status for the bot {Bot-Owner Only}."""
    await bot.change_presence(activity=discord.Streaming(name="whatever", url="https://twitch.tv/discordapp"))
    
@bot.command()
@commands.is_owner()
async def listen(ctx, *, title : str):
     """Listening status for the bot {Bot-Owner Only}."""
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="whatever"))

@bot.command()
@commands.is_owner()
async def watch(ctx, *, title : str):
     """Watching status for the bot {Bot-Owner Only}."""
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="whatever"))
