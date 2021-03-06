from os import name
from typing import Collection
import discord
from discord import client
from discord import message
from discord import colour
from discord.colour import Colour
from discord.ext import commands
from discord.ext.commands.errors import CheckAnyFailure
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import tord

class Informational(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['h'])
    async def help(self, ctx):
        """ Shows all the commands. """
        color = discord.Colour.dark_red()

        Info = discord.Embed(title='Informational Section', description='This is where all the informative commands are.', colour=color)
        Info.add_field(name='Help', value='`Showcases all the commands.`', inline=False)
        Info.add_field(name='Serverinfo', value='`Gives info on the current guild your in.`', inline=False)

        Useless = discord.Embed(title='Useless Section', description='This is where all the useless stuff is, lol.', colour=color)
        Useless.add_field(name='Ping', value='`Pong! (Gets the bots latency.)`', inline=False)
        Useless.add_field(name='Hello', value='`Says hello back.`', inline=False)
        Useless.add_field(name='Server', value='`The bots community server.`', inline=False)
        Useless.add_field(name='Avatar', value='`Gets your avatar or mentioned user.`', inline=False)
        Useless.add_field(name='Advertisements', value='`Just some stuff that is advertised on the bot.`', inline=False)

        Moderate = discord.Embed(title='Moderation Section', description='This is where all the moderation commands are.', colour=color)
        Moderate.add_field(name='Kick', value='`Kicks the mentioned member.`', inline=False)
        Moderate.add_field(name='Ban', value='`Bans the mentioned member.`', inline=False)
        Moderate.add_field(name='Unban', value='`Unbans the given username and discriminator.`', inline=False)
        Moderate.add_field(name='Purge', value='`Purges the messages given.(100 is the limit.)`', inline=False)
        Moderate.add_field(name='Mute', value='`Mutes the mentioned user. (If no role will create(Any bugs, contact the server))`', inline=False)
        Moderate.add_field(name='Unmute', value='`Unmutes the mentioned user.`', inline=False)
        Moderate.add_field(name='Slowmode', value='`Sets a channels slowmode.`', inline=False)
        Moderate.add_field(name='Rename', value='`Renames current channel your in.`', inline=False)
        Moderate.add_field(name='Create', value='`Creates a channel in the current guild your in.`', inline=False)
        Moderate.add_field(name='Delete', value='`Deletes the current channel your in.`', inline=False)

        Utility = discord.Embed(title='Utility Section', description='This is where all the utility commands are.', colour=color)
        Utility.add_field(name='Setprefix', value='`Changes the guilds prefix.`', inline=False)

        # Economy = discord.Embed(title='Economy Section', description='This is where all the economy commands are.', colour=color)
        # Economy.add_field(name='Balance', value='`Gets your money balance.`', inline=False)
        # Economy.add_field(name='Beg', value='`Beg for money from strangers, lol.`', inline=False)
        # Economy.add_field(name='Withdraw', value='`Withdraw some money from the bank.`', inline=False)
        # Economy.add_field(name='Deposit', value='`Deposit some money from the wallet.`', inline=False)
        # Economy.add_field(name='Give', value='`Give somebody some money.(From your wallet only, lol.)`', inline=False)
        # Economy.add_field(name='Rob', value='`Rob someone of their money/coins.', inline=False)

        Tordified = discord.Embed(title='Tordified Secftion', description='This is where all the tordified commands are.', colour=color)
        Tordified.add_field(name='Norway', value='`Plays a special audio. :)`', inline=False)
        Tordified.add_field(name='Tord', value='`Sends special gif/video. :)`', inline=False)
        Tordified.add_field(name='Tordbot', value='`Plays a special audio. :)`', inline=False)

        embeds = [
            Info,
            Useless,
            Moderate,
            Utility,
            Tordified
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()

    @commands.command(aliases=['si', 'guildinfo', 'gi', 'sinfo', 'ginfo'])
    async def serverinfo(self, ctx):
        roles = len(ctx.guild.roles)
        bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        color = discord.Colour.dark_red()

        ServerInfo = discord.Embed(rimestamp=ctx.message.created_at, title=f'Current Guild Information', color=color)
        ServerInfo.add_field(name='Server Name:', value=f'{ctx.guild.name}')
        ServerInfo.add_field(name='Verification Level', value=str(ctx.guild.verification_level))
        ServerInfo.add_field(name='Member Count:', value=ctx.guild.member_count)
        ServerInfo.add_field(name='Role Count:', value=str(roles))
        ServerInfo.add_field(name='Highest Role:', value=ctx.guild.roles[-1])
#       ServerInfo.add_field(name='Bot Count:', value=', '.join(bots))

        await ctx.send(embed=ServerInfo)

def setup(client):
    client.add_cog(Informational(client))