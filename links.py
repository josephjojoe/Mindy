import os
import discord
from discord.ext import commands

class Links(commands.Cog, name = "Link Commands"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='linkedin', help='Sends a link to Linkedin')
    async def linkedin(ctx):
        await ctx.send("linkedin.com")

    @commands.command(name='reddit', help="Sends a link to Reddit")
    async def reddit(ctx):
        await ctx.send("https://reddit.com")

    @commands.command(name='instagram', help="Sends a link to Instagram")
    async def instagram(ctx):
        await ctx.send("https://instagram.com")

    @commands.command(name='twitter', help="Sends a link to Twitter")
    async def twitter(ctx):
        await ctx.send("https://twitter.com")

    @commands.command(name='discord', help="Sends a link to Discord, although you're already here!")
    async def discord(ctx):
        await ctx.send("https://discord.com")

    @commands.command(name='facebook', help="Sends a link to Facebook")
    async def facebook(ctx):
        await ctx.send("https://facebook.com")

    @commands.command(name='tumblr', help="Sends a link to Tumblr")
    async def tumblr(ctx):
        await ctx.send("https://tumblr.com")
            
def setup(bot):
    bot.add_cog(Links(bot))
    print("Links cog is loaded. ")
