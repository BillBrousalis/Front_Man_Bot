#!/usr/bin/env python3
import discord
from discord.ext import commands

# Bot token removed before posting on github
# Front Man thinks about SECURITY!
BOT_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

cog_extensions = ['cogs.meme_cog', 'cogs.games_cog', 'cogs.math_crypto_cog', 'cogs.events_cog', 'cogs.misc_cog']

if __name__ == '__main__':
    bot = commands.Bot(command_prefix='.')
    bot.remove_command('help')
    for extension in cog_extensions:
        bot.load_extension(extension)
    bot.run(BOT_TOKEN)
