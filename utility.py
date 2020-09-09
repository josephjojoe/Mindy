import os
import discord
from discord.ext import commands

class Utility(commands.Cog, name = "Utility Commands"):

    def __init__(self, bot):
        self.bot = bot

    # Ping command
    @commands.command(name='ping', help="Shows ping time in milliseconds")
    async def ping(ctx):
        await ctx.send(f'Pong! That took {round(bot.latency*1000,2)}ms') # Bot.latency is in seconds

    # Returns User ID
    @commands.command(name='id', help="Returns user's Discord User ID")
    async def id(ctx):
        await ctx.send(f"{ctx.author.mention}'s ID = {ctx.author.id}") # Sends their Discord User ID

    # Links to my Github
    @commands.command(name='creatorgithub', help="Links to the Github of Mindy's creator")
    async def creatorgithub(ctx):
        await ctx.send("https://github.com/josephjojoe")

    # Links to Mindy's source code
    @commands.command(name='sourcecode', help="Links to Mindy's source code (Github)")
    async def mindysourcecode(ctx):
        await ctx.send("https://github.com/josephjojoe/Mindy")

    # General server info
    @commands.command(name='serverinfo', help="Shows general info about the server")
    async def id(ctx):
        prettyTime = ctx.author.guild.created_at.strftime('%A %d %B %Y') # Time of creation
        await ctx.send(f"""```Server Name: {ctx.author.guild}
    Description: {ctx.guild.description}
    Member Count: {ctx.guild.member_count}
    Creation Date: {prettyTime}```""") # Needs variable to work

    # Member count
    @commands.command(name='membercount', help="Returns the number of members in the server")
    async def membercount(ctx):
        await ctx.send(f"Member count of {ctx.guild}: {ctx.guild.member_count}")

    # Invite link for bot
    @commands.command(name='botinvite', help="Sends a link to invite Mindy to your own server")
    async def botinvite(ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=750245181667934219&permissions=8&scope=bot")

    # Invite link for server
    @commands.command(name='invite', aliases=['invitelink', 'serverinvite', 'serverlink'], help="Returns a server invite link that lasts for one hour")
    async def serverinvite(ctx):
        serverInviteLink = await ctx.channel.create_invite()
        await ctx.send(serverInviteLink)

def setup(bot):
    bot.add_cog(Utility(bot))
    print("Utility cog is loaded. ")
