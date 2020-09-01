import os
import discord
from discord.ext import commands # Imports dependencies
import dotenv
from dotenv import load_dotenv

# Loads token from .env file
load_dotenv()
token = os.getenv('TOKEN')

# Mindy description
description = 'Mindy is a no-nonsense minimal bot. Keeping it simple with moderation and utility commands, and nothing more.'

# Prefix and description
bot = commands.Bot(command_prefix = 'mindy', description=description)

# When bot is ready
@bot.event
async def on_ready():
    print("Mindy is ready.")

#
# Utility commands
#

# TO DO:
# invite link command for bot
# invite link command for server
# github command
# general server info
# amount of members command
# ping command
#
#
#

bot.run(token)
