import os
import discord
from discord.ext import commands

class Moderation(commands.Cog, name="Moderation Commands"):

    def __init__(self, bot):
        self.bot = bot

    # Kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None): 
        try:
            await user.kick(reason=reason)
            await ctx.send(f"{user} was kicked from the server.")
        except discord.Forbidden:
            await ctx.send("Sorry, you don't have permissions to do this.")
        
    # Ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None): 
        try:
            await member.ban(reason=reason)
            await ctx.send(f"{member} was banned from the server.")
        except commands.Forbidden:
            await ctx.send("Sorry, you don't have permissions to do this.")


def setup(bot):
    bot.add_cog(Moderation(bot))
    print("Moderation cog is loaded. ")
