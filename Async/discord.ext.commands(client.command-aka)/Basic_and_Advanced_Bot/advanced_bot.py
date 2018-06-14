import discord, asyncio
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix="<your_prefix>")

@client.event
async def on_ready():
    print("Bot Is Ready!")
    await client.change_presence(game=discord.Game(name=f"{len(client.get_all_members())} Players!", type=2))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context=True, hidden=True)
async def shutdown(ctx):
    if ctx.message.author.id == "<your_id>":
        await client.say("im shutting down, goodbye!")
        await client.logout()

@client.command(pass_context=True)
async def userinfo(ctx, user: discord.User): #notice how i added for mentioning user
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
async def kick(ctx, user: discord.User, *, reason: str):
    if "<staff_role_id>" in [role.id for role in ctx.message.author.roles]:
        await client.kick(user)
        await client.say(f"boom, user has been kicked for reason: {reason}")

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    if "<staff_role_id>" in [role.id for role in ctx.message.author.roles]:
        await client.ban(user)
        await client.say(f"{user.name} Has been Banned! Let's hope he will never come back again lol.")

@client.command(pass_context=True)
async def warn(ctx, user: discord.Member):
    if "<staff_role_id>" in [role.id for role in ctx.message.author.roles]:
        embed = discord.Embed(title="WARNING!", description="Please be sure to read Rules so you don't break anything again!", color=0xFFF000)
        embed.add_field(name=f"{user.name} Has been Warned", value="<want to put another thing here? just edit it and put it>")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def playing(ctx, type1: str, *, status: str):
    if ctx.message.author.id == "<your_id>":
        #in type1, we add a number for the type, and in status, we want to addd on what will it show
        #now the things
        await client.change_presence(game=discord.Game(name=f"{status}", type=type1))
        await bot.say("Done!") #we want the bot to say once its done!

#so if we execute in this ^ '[p]playing 2 Server' ([p] is your prefix) the bot wil change into "Listening Into Server"

client.run("token")
