'''as in the on_message, we have this, which it can be still done to discord.ext.commands:'''
#this code will demonstrate on adding up a playing status for the bot

#now lets add a simple playing status when the bot is ready!
@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(game=discord.Game(name="It's a bot"))

#now let's try something different, this one we are going to put a streaming status
'''if you already have the:
@client.event
async def on_ready():, DO NOT ADD IT AGAIN!!
alright here let's make it!'''
@client.event
async def on_ready():
    print("Bot Is Ready!")
    await client.change_presence(game=discord.Game(name="With Players!", url="https://twitch.tv/T", type=1)) #the url is needen so it can show the actual streaming status, if not putten, it will show a playing on PC and when you click on profile, it will show streaming, so in conclusion, adding url makes it show a streaming status!

#now lets do an advanced one where we are going to count members the bot is "Listening"
@client.event
async def on_ready():
    print("Bot Is Ready!")
    await client.change_presence(game=discord.Game(name=f"{len(client.get_all_members())} Players!", type=2))

'''so now let's make a command so that only you can change the status of the bot, the type and etc.'''
@client.command(pass_context=True)
async def playing(ctx, type1: str, *, status: str):
    if ctx.message.author.id == "<your_id>":
        #in type1, we add a number for the type, and in status, we want to addd on what will it show
        #now the things
        await client.change_presence(game=discord.Game(name=f"{status}", type=type1))
        await bot.say("Done!") #we want the bot to say once its done!

#so if we execute in this ^ '[p]playing 2 Server' ([p] is your prefix) the bot wil change into "Listening Into Server"
#that should explain it all for now!
