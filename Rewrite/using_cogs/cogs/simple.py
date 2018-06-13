# basic cog
import discord
from discord.ext import commands


"""A simple cog example with simple commands. Some with the use of events in cogs.
Rewrite docs:
http://dischttp://discordpy.readthedocs.io/en/rewrite/
You could also create your own custom checks. Check out:
https://github.com/Rapptz/discord.py/blob/master/discord/ext/commands/core.py#L689
For a list of events:
http://discordpy.readthedocs.io/en/rewrite/api.html#event-reference
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#event-reference
"""


class Simple:
    """Some simple commands for the rewrite cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, ctx, *, our_input: str):
        """A simple command which repeats our input.
        In rewrite Context is automatically passed to our commands as the first argument after self."""

        await ctx.send(our_input)

    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        """A simple command which does addition on two integer values."""

        total = first + second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='embeds')
    @commands.guild_only()
    async def example_embed(self, ctx):
        """A simple command which showcases the use of embeds.
        Try changing colors and names etc."""

        embed = discord.Embed(title='Example Embed',
                              description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                              colour=0x98FB98)
        embed.set_author(name='GeorgeCY',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='https://www.w3schools.com/w3css/w3css_images.asp')
        embed.set_image(url='https://www.google.no/imgres?imgurl=https%3A%2F%2Fthemeawesome.com%2Fthemes%2Ftotalpress%2Fwp-content%2Fuploads%2F2012%2F12%2Funicorn-wallpaper.jpg&imgrefurl=https%3A%2F%2Fthemeawesome.com%2Fthemes%2Ftotalpress%2Fpost-format-image%2F&docid=a0UGZeBM_0JzLM&tbnid=ZPIb9IX5WOejGM%3A&vet=10ahUKEwjGy8-56dDbAhXBKJoKHVccA_0QMwhnKA4wDg..i&w=1600&h=1200&bih=974&biw=1920&q=image&ved=0ahUKEwjGy8-56dDbAhXBKJoKHVccA_0QMwhnKA4wDg&iact=mrc&uact=8')
        
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)

    async def on_member_ban(self, guild, user):
        """Event Listener which is called when a user is banned from the guild.
        This will print some stuff into the console
        """

        print(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case Simple.
# When we load the cog, we use the name of the file.
# Remember to have the bot parameter, and run the bot.add_cog.
# You could have the cog inside the main file just with bot.add_cog(ClassName(bot)).
def setup(bot):
    bot.add_cog(Simple(bot))
