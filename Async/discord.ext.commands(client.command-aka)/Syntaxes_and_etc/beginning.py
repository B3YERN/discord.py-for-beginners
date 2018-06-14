#this is the beginning of making discord.ext.commands[@client.command()]
'''now lets demonstrate the syntax which its:
@client.command(pass_context=True)
async def command(ctx, args):
    #await tasks
    #if necessary, more tasks'''
#now lets make some examples by making a simple ping command

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

'''this is a basic of making a command, you can also give it things like args
so now lets make a hidden command, let's take this example:'''

@client.command(pass_context=True, hidden=True) #notice how i added 'hidden=True' into client.command()
async def shutdown(ctx):
    if ctx.message.author.id == "<your_id>":
        await client.say("im shutting down, goodbye!")
        await client.logout()

'''now there are more things you can do but for now on, let's get into using
args (arguements), lets have this userinfo example here:'''
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
'''so now once a user in mentioned, it will show info, and it will also have an
automatic color embed right here!'''

'''now lets get into more things for using args
lets make this kick command with reason providing:
[NOTE: i will be making a moderation.py for usage of moderation commands like:
warn and etc.]'''
@client.command(pass_context=True)
async def kick(ctx, user: discord.User, *, reason: str): #notice how we added more things
    await client.kick(user)
    await client.say(f"boom, user has been kicked for reason: {reason}")

'''you can also look for more arguements in: http://discordpy.readthedocs.io/en/latest/api.html#data-classes'''
