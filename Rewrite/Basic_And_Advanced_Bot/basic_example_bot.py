import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='any_prefix_as_much_as_you_want_')
client = discord.Client()


@bot.event
async def on_ready():
  print('My son has been awaken from dead')
  
@bot.command()
async def cookie(ctx):
"""Cookie from your son"""
  await ctx.send(":cookie:")
  
@bot.command()
async def ping(ctx):
"""Ping pong"""
  await ctx.send("ctx.message.author.mention, Pong")

bot.run(' ')
