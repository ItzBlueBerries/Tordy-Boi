from typing import Collection
import discord
from discord import client
from discord import message
from discord.colour import Color
from discord.embeds import Embed
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

    @commands.command(aliases=['ava', 'profilepic'])
    async def avatar(self, ctx, member : discord.Member = None):
        if member == None:
            member = ctx.author
        
        ava = member.avatar_url
        color = discord.Colour.dark_red()

        AvatarEmbed = discord.Embed(title=f'{member.name}\'s Avatar', color=color)
        AvatarEmbed.set_image(url=ava)

        await ctx.send(embed=AvatarEmbed)

    @commands.command(aliases=['ads'])
    async def advertisement(self, ctx):
        ads = discord.Embed(
            title='Tordy Boi Advertisements',
            color=discord.Colour.dark_red()
        )

        ads.set_image(url='https://i.quotev.com/img/q/u/17/5/3/3qrpzqm4fv.jpg')
        ads.add_field(name='Fruitsy Bot Testing Server', value='[I was born here, and I am tested there lol.](https://discord.gg/gX3JRNedXd)')
        ads.add_field(name='Reality Engine', value='[Ay, a server for an fnf engine..? THAT MY CREATOR MADE? lol](https://discord.gg/NWaaPpgvjp)')
        ads.add_field(name='Fruitsy\'s Modding Club', value='[A fnf modding server that my creator made, go join lol.](https://discord.gg/JzcAAHVJE7)')

        await ctx.send(embed=ads)

    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
        color = discord.Colour.dark_red()

        inviteEmbed = discord.Embed(title='Bot Invite', description=f'[Here is my invite! Go add me to your server if you want lol.](https://discord.com/api/oauth2/authorize?client_id=862605357284982784&permissions=8&scope=bot)', colour=color)
        await ctx.send(embed=inviteEmbed)

def setup(client):
    client.add_cog(Useless(client))