import discord
from discord.ext import commands
import math

class misc_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['help', 'Help', 'HELP', 'commands', 'Commands', 'COMMANDS'])
    async def _help(self, ctx):
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            return None
        commands = '\n'.join(['**Games:**', '.marbles', '.ddakji',
                    '**Math/Crypto:**', '.calc', '.base64', '.rot13',
                    '**Memes:**', '.meme',
                    '**Misc:**', '.help', '.latency'])
        embedVar = discord.Embed(title="Bot Commands:", description=commands, color=0xfcba03)
        await ctx.channel.send(embed=embedVar)

    @commands.command()
    async def latency(self, ctx):
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            return None
        await ctx.send(f"Latency: {math.floor(self.bot.latency *1000)} ms")
        
def setup(bot):
    bot.add_cog(misc_cog(bot))
