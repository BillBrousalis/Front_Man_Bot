import discord
from discord.ext import tasks, commands
import random

class events_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()

    @tasks.loop(minutes=30)
    async def change_status(self):
        s = ['Front Man is the BOSS!',
             'Front Man RULES!',
             'Front Man can CODE!',
             'Front Man FTW!']
        next = random.choice(s)
        while next == self.status:
            next = random.choice(s)
        self.status = next
        await self.bot.change_presence(activity=discord.Game(self.status))
    
def setup(bot):
    bot.add_cog(events_cog(bot))