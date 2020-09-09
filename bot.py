import os
import sys
import discord
from discord.ext import commands # Imports dependencies
import dotenv
from dotenv import load_dotenv

# Loads token from .env file
load_dotenv()
token = os.getenv('TOKEN')

# Mindy description and command prefix
description = 'Mindy is a no-nonsense minimal bot. Keeping it simple with moderation and utility commands, and nothing more.'
bot = commands.Bot(command_prefix = 'mindy ', description=description)

# Loads cogs
bot.load_extension('utility')
bot.load_extension('links')

# When bot is ready
@bot.event
async def on_ready():
    print("Mindy is ready.")
    
# Runs bot with token
bot.run(token)
