from typing import Collection
import discord
from discord import client
from discord import message
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure
import asyncio

class Tordified(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def norway(self, ctx):
        voice = ctx.author.voice

        if voice is None:
            await ctx.send('You are not in a voice channel, please join one first..')
            return
        
        voice2 = await ctx.author.voice.channel.connect()
        voice2.play(discord.FFmpegPCMAudio(executable="D:/PATH_Programs/ffmpeg.exe", source="D:/TordyBoi/assets/music/norway.mp3"))
        await ctx.send('Starting up some norway... :)')
        await asyncio.sleep(18.8)
        await ctx.voice_client.disconnect()

    @commands.command()
    async def tord(self, ctx):
        with open('D:\\TordyBoi\\assets\\videos\\tord.mp4', 'rb') as tordy:
            tordyboi = discord.File(tordy)

        await ctx.send('Tordy Booiiiiiiiiiiiiiiiii', file=tordyboi)

    @commands.command()
    async def tordbot(self, ctx):
        voice = ctx.author.voice

        if voice is None:
            await ctx.send('You are not in a voice channel, please join one first..')
            return
        
        voice2 = await ctx.author.voice.channel.connect()
        voice2.play(discord.FFmpegPCMAudio(executable="D:/PATH_Programs/ffmpeg.exe", source="D:/TordyBoi/assets/music/tordbot.mp3"))
        await ctx.send('Starting up some tordbot... :)')
        await asyncio.sleep(50.8)
        await ctx.voice_client.disconnect()

def setup(client):
    client.add_cog(Tordified(client))