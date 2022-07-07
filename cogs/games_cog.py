import discord
from discord.ext import commands
import time
import random

class games_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def marbles(self, ctx):
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            return None
        guess = ctx.message.content.replace('.marbles', '')
        r = random.choice(["        EVEN    \U0001F52E    \U0001F52E", "ODD   \U0001F52E    \U0001F52E    \U0001F52E"])
        time.sleep(1.5)
        if (("EVEN" in guess) or ("ODD" in guess)) and not (("EVEN" in guess) and ("ODD" in guess)):
            res = f"Turns hand around: ||**   {r}   **||"
        else:
            res = "**Example :**\n.marbles ODD\nor\n.marbles EVEN"
        await ctx.send(res)




    @commands.command(aliases=['ddakji', 'Ddakji', 'DDAKJI'])
    async def _ddakji(self, ctx):
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            return None
        response_pool = ["You hit the tile on the floor with yours with all the power you got...\nThe tile flies up in the air and...",
                         "You take your time to aim at the tile on the floor for a clean hit...\nYou throw yours and...",
                         "You strike the tile on the floor with a combination of power and precision...\nThe tile jumps up in the air and..."]
        await ctx.send(random.choice(response_pool))
        time.sleep(2)
        outcome = ["It lands flipped! Nice!", 
                   "It lands straight back without flipping! Unlucky!"]
        await ctx.send(f"|| {random.choice(outcome)} ||")

def setup(bot):
    bot.add_cog(games_cog(bot))