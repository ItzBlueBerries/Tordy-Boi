import discord
from discord.ext import commands
import asyncio

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Connecting...')
        await asyncio.sleep(0.5)
        print('BotConnection ----> Tordy Boi!')


def setup(client):
    client.add_cog(Events(client))