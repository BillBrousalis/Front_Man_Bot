import discord
from discord.ext import commands
import random
import praw
import praw.models

# Account information removed!
# Front Man doesn't publish his credentials!
reddit = praw.Reddit(client_id = "XXXXXXXXXXX",
                    client_secret = "XXXXXXXXXXXXXXXXXX",
                    username = "XXXXXXXXXXX",
                    password = "XXXXXXXXXXXXXXXX",
                    user_agent = "XXXXXXXXXXXXXXXX",
                    check_for_async=False)

class meme_cog(commands.Cog):
    def __init__(self, bot):
        self.reddit = reddit
        self.bot = bot

    # fetch random meme from reddit's
    # dankmemes subreddit
    @commands.cooldown(1, 2, commands.BucketType.guild)
    @commands.command(aliases=['meme', 'Meme', 'MEME'])
    async def _meme(self, ctx):
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            return None
        subreddit = self.reddit.subreddit("dankmemes")
        all_submissions = []
        hot = subreddit.hot(limit = 200)
        for submission in hot:
            if submission.stickied == False:
                all_submissions.append(submission)
        random_submission = random.choice(all_submissions)
        name = random_submission.title
        url = random_submission.url
        embedMeme = discord.Embed(title=name).set_image(url=url)
        await ctx.send(embed=embedMeme)

def setup(bot):
    bot.add_cog(meme_cog(bot))
