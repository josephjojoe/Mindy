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
bot = commands.Bot(command_prefix = 'mindy ', description=description)

# When bot is ready
@bot.event
async def on_ready():
    print("Mindy is ready.")

#
# Utility commands
#

# Ping
@bot.command(name='ping', help="Shows ping time in milliseconds")
async def ping(ctx):
    await ctx.send('Pong! That took {0}ms'.format(round(bot.latency * 1000,1)))

# General server info
@bot.command(name='serverinfo', help="Shows general info about the server")
async def id(ctx):
    prettyTime = ctx.author.guild.created_at.strftime('%A %d %B %Y') # Time of creation
    await ctx.send(f"""```Server Name: {ctx.author.guild}
Description: {ctx.author.guild.description}
Member Count: {ctx.author.guild.member_count}
Creation Date: {prettyTime}```""") # Needs variable to work

# Member count
@bot.command(name='membercount', help="Returns the number of members in the server")
async def membercount(ctx):
    await ctx.send(f"Members in {ctx.author.guild}: {ctx.author.guild.member_count}")

# Invite link for bot
@bot.command(name='botinvite', help="Sends a link to invite Mindy to your own server")
async def botinvite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=750245181667934219&permissions=8&scope=bot")

# Invite link for server
@bot.command(name='invite', help="Returns a server invite link that lasts for one hour")
async def serverinvite(ctx):
    await ctx.send(ctx.author.guild.create_invite(max_age = 3600))



# TO DO:
# 
# invite link command for server, fix it
# github command (link to github.com/josephjojoe)
# 
# 
# 
#
#
#

bot.run(token)
