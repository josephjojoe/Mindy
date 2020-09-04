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

# Ping command
@bot.command(name='ping', help="Shows ping time in milliseconds")
async def ping(ctx):
    await ctx.send(f'Pong! That took {round(bot.latency*1000,2)}ms') # Bot.latency is in seconds

# Returns User ID
@bot.command(name='id', help="Returns user's Discord User ID")
async def id(ctx):
    await ctx.send(f"{ctx.author.mention}'s ID = {ctx.author.id}") # Sends their Discord User ID

# Links to my Github
@bot.command(name='creatorgithub', help="Links to the Github of Mindy's creator")
async def creatorgithub(ctx):
    await ctx.send("https://github.com/josephjojoe")

# Links to Mindy's source code
@bot.command(name='sourcecode', help="Links to Mindy's source code (Github)")
async def mindysourcecode(ctx):
    await ctx.send("https://github.com/josephjojoe/Mindy")

# General server info
@bot.command(name='serverinfo', help="Shows general info about the server")
async def id(ctx):
    prettyTime = ctx.author.guild.created_at.strftime('%A %d %B %Y') # Time of creation
    await ctx.send(f"""```Server Name: {ctx.author.guild}
Description: {ctx.guild.description}
Member Count: {ctx.guild.member_count}
Creation Date: {prettyTime}```""") # Needs variable to work

# Member count
@bot.command(name='membercount', help="Returns the number of members in the server")
async def membercount(ctx):
    await ctx.send(f"Member count of {ctx.guild}: {ctx.guild.member_count}")

# Invite link for bot
@bot.command(name='botinvite', help="Sends a link to invite Mindy to your own server")
async def botinvite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=750245181667934219&permissions=8&scope=bot")

# Invite link for server
@bot.command(name='invite', aliases=['invitelink', 'serverinvite', 'serverlink'], help="Returns a server invite link that lasts for one hour")
async def serverinvite(ctx):
    serverInviteLink = await ctx.channel.create_invite()
    await ctx.send(serverInviteLink)



# TO DO:
# 
# 
# 
# 
# 
# 
#
#
#

bot.run(token)
