import discord
from discord.ext import commands
import base64

class math_crypto_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx):
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            return None
        msg = ctx.message.content.replace('.calc', '')
        try:
            res = f'Result: {str(eval(msg))}'
        except Exception:
            res = f'Something went wrong ...\nYour request : {msg}\nExample : .calc 100 + 100 / 3'
        await ctx.send(res)

    @commands.command()
    async def base64(self, ctx):
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            return None
        msg = ctx.message.content.replace('.base64', '')
        if '-d' in msg:
            msg = msg.replace('-d', '').strip()
            try:
                res = f'"{msg}" decoded :\n{base64.b64decode(msg.encode()).decode()}'
            except:
                res = 'Something went wrong ...'  
        elif '-e' in msg:
            msg = msg.replace('-e', '').strip()
            try:
                res = f'"{msg}" encoded :\n{base64.b64encode(msg.encode()).decode()}'
            except Exception:
                res = 'Something went wrong ...'
        else:
            res = '**Example :**\n.base64 -d YmFzZTY0IHJvY2tzIQ==\n or \n.base64 -e base64 rocks!\n(-d for decoding or -e for encoding)'
        await ctx.send(res)

    @commands.command()
    async def rot13(self, ctx):
        if not isinstance(ctx.channel, discord.channel.DMChannel):
            return None
        msg = ctx.message.content.replace('.rot13', '').strip()
        if msg != '':
            rot13 = str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
                                  "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
            res = f'"{msg}" -> rot13 :\n{str.translate(msg, rot13)}'
        else:
            res = '**Example :**\n.rot13 This is my sample text!'
        await ctx.send(res)
            
def setup(bot):
    bot.add_cog(math_crypto_cog(bot))
