'''A way to make your bot become advanced


embed = discord.Embed(title = 'Test Embed', description = 'hello world')
embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too

# Images
embed.set_image(url = 'Image Url')
embed.set_thumbnail(url = 'Image Url')

embed.set_author('Author name', url = 'Url to author', icon_url = 'Image Url') # appears on top
embed.set_footer(text = 'Example footer', icon_url = 'Image Url') 
embed.timestamp = datetime.datetime.utcnow() 

embed.add_field('Field name [256 char max]', 'Content [1024 char]', inline=True) 
# max 25 fields


# to confirm that it's embed:
await ctx.send(embed=embed)
 # or: await channel.send(embed=embed)
 
 
# Random Images with embed
@bot.command()
async def URL(ctx):
    """You gonna enjoy some shitpost"""
    embed = discord.Embed(colour=000000)
    embed.set_image(url=random.choice("URL1 , URL2 "]))
    await ctx.send(embed=embed)
    
# Help command with embed (you will have to remove your help command).
@bot.command()
async def help(ctx):
    """Help me"""
    embed = discord.Embed(colour=000000)
    embed.set_author('Geor + ge = George', url = 'https://imgix.ranker.com/user_node_img/50054/1001066706/original/the-mortiest-morty-is-very-special-photo-u1?w=650&q=50&fm=jpg&fit=crop&crop=faces', icon_url = 'https://scontent-frt3-2.cdninstagram.com/vp/cf6cc2917de3995f9398f7ea70711846/5BA4DC58/t51.2885-15/e35/29093958_151991522147625_8360402945472200704_n.jpg?se=7&ig_cache_key=MTczMzUyNjgyMDkxMDkwNzI0NQ%3D%3D.') # appears on top
    embed.set_footer(text = 'Command1', description='whatever') 
    embed.set_footer(text = 'Command2', description='whatever') 
    embed.set_footer(text = 'Command3', description='whatever') 
    embed.set_footer(text = 'Command4', description='whatever') 
    embed.set_footer(text = 'Command5', description='whatever') 
    
