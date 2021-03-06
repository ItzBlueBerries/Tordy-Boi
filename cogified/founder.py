from typing import Collection
import discord
from discord import client
from discord import message
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure

class Founder(commands.Cog):

    def __init__(self, client):
        self.client = client


    # @commands.command(aliases=['leave_guild'])
    # @commands.is_owner()
    # async def leave(self, ctx, guild):
    #     await guild.leave()
    #     await ctx.send(f"__***Left guild Successfully***__\n*{guild.name} ({guild.id})*")

    @commands.command(aliases=['kill', 'quit', 'close'])
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Shutting down..')
        await self.client.close()
        print('Tordy Boi has shutdown successfully..')

def setup(client):
    client.add_cog(Founder(client))