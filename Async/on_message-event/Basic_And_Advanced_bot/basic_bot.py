#a basic bot by GeorgeCY!
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix="prefix_goes_here!")

@client.event
async def on_ready():
    print("Bot is Ready!")

@client.event
async def on_message(message):
    if message.content == "ping":
        await client.send_message(message.channel, "Pong!")
    if message.content.startswith("cookie"):
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper().startswith("COMMAND"):
        await client.send_message(message.channel, "what?")
   
client.run("token_here")
