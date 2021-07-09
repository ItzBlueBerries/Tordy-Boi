from typing import Collection
import discord
from discord import client
from discord import message
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure
import tord
import json

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['prefix'])
    async def setprefix(self, ctx, prefixset=None):
        if (not ctx.author.guild_permissions.administrator):
            await ctx.send('Yeah, you don\'t have the `ADMINISTRATOR` permission, lol.')
            return

        if (prefixset == None):
            prefixset = 't!'

        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefixset

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f' Tordy Boi Prefix: `{prefixset}` ')


def setup(client):
    client.add_cog(Utility(client))