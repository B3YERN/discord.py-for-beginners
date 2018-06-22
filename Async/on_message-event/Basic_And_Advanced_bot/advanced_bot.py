#advanced bot by GeorgeCY
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix="prefix_goes_here!")

@client.event
async def on_ready():
    print("Bot Is Ready!")
    await client.change_presence(game=discord.Game(name=f"{len(client.get_all_members())} Players!", type=2))

@client.event
async def on_message(message):
    if message.content == "ping":
        await client.send_message(message.channel, "Pong!")
    if message.content.startswith("cookie"):
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper().startswith("COMMAND"):
        await client.send_message(message.channel, "what?")
    if message.content.upper().startswith("HELLO"):
        embed1 = discord.Embed(title="Message Bot", description=f"Hello {message.author.name}, How are you?", color=message.author.color)
        embed1.set_thumbnail(url=message.author.avatar_url)
        embed1.set_footer(text="this was introduced for an example embed!")
        await client.send_message(message.channel, embed=embed1)

client.run("token")
