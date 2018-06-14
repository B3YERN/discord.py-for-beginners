'''Moderation examples (DO NOT COPY AND PASTE IT, JUST EDIT IT ON YOUR SCRIPT)'''


'''To script kick command you will need to have member arguement and use member.kick()'''

'''You can take this script for your bot by editing'''

@bot.command()
async def kick(ctx, *, member : discord.Member = None):
    """Kick the client at the server."""
    try:
        await member.kick()
        await ctx.send("Whatever you want to say")
    except discord.errors.Forbidden:
        await ctx.send('I don\'t have perms')
      
'''To make ban command you will also need to use member arguement and able to use ctx.guild.ban(member)'''   
@bot.command()
async def ban (ctx, member:discord.Member):
    """Bans the client with mention."""
    await ctx.guild.ban(member)
    await ctx.send(f"Bitch,{member.mention} has been banned!")
    
'''Alright I'll be giving mutiple examples of mute/unmute and you will able to choose one of them to use it and also you will need to setup Muted Role on your server'''


'''Here we have role.name to choose any name of roles'''

@bot.command()
async def mute(ctx, member:discord.Member):
    """Mute the client on the server."""
    if "Hey Vsauce michael here" in [role.name for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        for each in ctx.guild.channels:
                await each.set_permissions(member, overwrite=overwrite)
                
 ''' And another we have is role.id, to use this you will need to copy ID of role'''
 
@bot.command()
async def mute(ctx, member:discord.Member):
    """Mute the client on the server."""
    if "ID Here" in [role.id for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        for each in ctx.guild.channels:
                await each.set_permissions(member, overwrite=overwrite) 
                
                
''' If you want to make it double role.name or id there's script for ya '''
                
                
                
@bot.command()
async def mute(ctx, member:discord.Member):
    """Mute the client on the server."""
    if "Staff" or "Choose any role name" in [role.name for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        for each in ctx.guild.channels:
                await each.set_permissions(member, overwrite=overwrite)

@bot.command()
async def mute(ctx, member:discord.Member):
    """Mute the client on the server."""
    if "Role ID 1" or "Role ID 2" in [role.id for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        for each in ctx.guild.channels:
                await each.set_permissions(member, overwrite=overwrite)
                
                
