import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix='any_prefix_as_much_as_you_want_')
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Servers or whatever you want"))

@bot.command()
async def cookie(ctx):
"""Cookie from your son"""
  await ctx.send(":cookie:")
  await ctx.message.add_reaction('\U0001f36a')
  
@bot.command()
async def ping(ctx):
"""Buy a new damn Wi-Fi Script Kiddy cunt"""
    resp = await ctx.send('Pong! Loading...')
    diff = resp.created_at - ctx.message.created_at
    await resp.edit(content=f'Pong! That took {1000*diff.total_seconds():.1f}ms.')
    
@bot.command()
async def dick_length(ctx):
  """Check how long is your dick before it grows cancer"""
  await ctx.send(f'Dick size of {ctx.author} is 8{"=" * random.randint(0, 50)}D')
  
@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
    
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(["Examples" ,"like" , "this" ,"dope" ,"rewrite" ,"tutorial"]))
    
@bot.command()
"""It's just a example of bot to type in"""
channel = bot.get_channel(Any ID)
await ctx.send('test')

@bot.command()
async def RDNG(ctx, dice: str):
    """Checks Random Number Generator in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
@commands.is_owner()              
async def die(ctx): 
        """Safely shuts down the bot"""

        await ctx.send("Shutting down...")
        await bot.logout()
        
@bot.command()
async def say(ctx, *, message):
    """Whatever the fuck you say, your son will treat you shit"""
    await ctx.send(message)
@bot.command()
async def userinfo(ctx, member : discord.Member):
    embed = discord.Embed(title="User Info for {}".format(member.name), colour=000000)
    embed.add_field(name="Username:", value=member.name, inline=True)
    embed.add_field(name="User ID:", value=member.id, inline=True)
    embed.add_field(name="Is Bot:", value=member.bot)
    embed.add_field(name="Created at:", value=member.created_at, inline=True)
    embed.add_field(name="Nickname:", value=member.display_name)
    embed.add_field(name='Status:', value=member.status, inline=True)
    embed.add_field(name="Playing:", value=member.game)
    embed.add_field(name="Highest Role:", value=member.top_role, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

bot.run('I like the way you tried to look for a token idiot')    
