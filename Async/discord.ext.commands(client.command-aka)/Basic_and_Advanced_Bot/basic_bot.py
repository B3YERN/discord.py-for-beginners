import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix="<your_prefix>")

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(game=discord.Game(name="It's a bot"))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context=True)
async def userinfo(ctx, user: discord.User):
    embed = discord.Embed(title="User Info for {}".format(user.name), color=user.color)
    embed.add_field(name="Username:", value=user.name, inline=True)
    embed.add_field(name="User ID:", value=user.id, inline=True)
    embed.add_field(name="Is Bot:", value=user.bot)
    embed.add_field(name="Created at:", value=user.created_at, inline=True)
    embed.add_field(name="Nickname:", value=user.display_name)
    embed.add_field(name="Status:", value=user.status, inline=True)
    embed.add_field(name="Playing:", value=user.game)
    embed.add_field(name="Highest Role:", value=user.top_role, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    if "<staff_role_id>" in [role.id for role in ctx.message.author.roles]:
        await client.kick(user)
        await client.say(f"{user.name} Has Been Kicked!")

client.run("token")
