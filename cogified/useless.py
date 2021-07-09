from typing import Collection
import discord
from discord import client
from discord import message
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure

class Useless(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        """ Ping, Pong! (Gets bots latency.) """
        await ctx.send(f'Pong! (Is this a testing command? :0 lol)\n**{round(self.client.latency * 1000)}ms**')

    @commands.command(aliases=['hi', 'heyo', 'hoi', 'hiya', 'helo', 'heya'])
    async def hello(self, ctx):
        """ Says hello to you! """
        await ctx.send(f'Hello there, {ctx.author}. I\'m Tordy..Nice meetin\' ya.')

    @commands.command(aliases=['community'])
    async def server(self, ctx):
        """ The community server for the bot. """
        await ctx.send('https://discord.gg/tWNAUsf5MW')


def setup(client):
    client.add_cog(Useless(client))