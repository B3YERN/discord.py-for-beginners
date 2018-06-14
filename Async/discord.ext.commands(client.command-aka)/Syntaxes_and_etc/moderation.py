'''here lets start with basic moderation commands
due to im lazy showing syntax let's start with basic moderation commands examples:'''

#a basic kick command
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    if "<staff_role_id>" in [role.id for role in ctx.message.author.roles]:
        await client.kick(user)
        await client.say(f"{user.name} Has Been Kicked!")

#a basic ban command
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    if "<staff_role_id>" in [role.id for role in ctx.message.author.roles]:
        await client.ban(user)
        await client.say(f"{user.name} Has been Banned! Let's hope he will never come back again lol.")

#and now a good basic warn command
@client.command(pass_context=True)
async def warn(ctx, user: discord.Member):
    if "<staff_role_id>" in [role.id for role in ctx.message.author.roles]:
        embed = discord.Embed(title="WARNING!", description="Please be sure to read Rules so you don't break anything again!", color=0xFFF000)
        embed.add_field(name=f"{user.name} Has been Warned", value="<want to put another thing here? just edit it and put it>")
        await client.say(embed=embed)
