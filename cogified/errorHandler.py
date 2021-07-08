import discord
from discord.ext import commands
import asyncio

class errorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing Arguments, try again.')
            return

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found, maybe you misspelled it?')
            return

        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('I am missing the required permissions.')
            return

        elif isinstance(error, commands.BadArgument):
            await ctx.send('Bad argument, maybe try doing it better next time?')
            return
        
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('This command is currently disabled.')
            return
        
        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send('Extension is already loaded.')
            return
        
        elif isinstance(error, commands.ExtensionError):
            await ctx.send('There was an error with the extension.')
            return
        
        elif isinstance(error, commands.ExtensionFailed):
            await ctx.send('The extension failed..maybe try again later.')
            return
        
        elif isinstance(error, commands.ExtensionNotFound):
            await ctx.send('Unknown extension, unable to find. TypeError?')
            return

        elif isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send('Extension not loaded, please load the extension first.')
            return
        
        elif isinstance(error, commands.MissingRole):
            await ctx.send('User is missing a certain role.')
            return
        
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the correct permissions to use this command.')
            return

        elif isinstance(error, commands.BotMissingRole):
            await ctx.send('I do not have the correct role to execute this command.')
            return
        
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Can not find the member that was supplied.')
            return
        
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('Cannot private message the user.')
            return

        elif isinstance(error, commands.NotOwner):
            await ctx.send('You are not the creator of me, you cannot use this command.')
            return
        
        elif isinstance(error, commands.MessageNotFound):
            await ctx.send('Message was not found.')
            return
        
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send('Role not found, try again?')
            return
        
        elif isinstance(error, commands.UserNotFound):
            await ctx.send('User was not found.')
            return
        
        elif isinstance(error, commands.EmojiNotFound):
            await ctx.send('Emoji not found...what emoji are you looking for exactly?')
            return

        elif isinstance(error, commands.GuildNotFound):
            await ctx.send('Cannot find the guild.')
            return
        
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send('Channel was not found.')
            return
        
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send('There is an invoke error.')
            return
        
        else:
            
            raise error

def setup(client):
    client.add_cog(errorHandler(client))