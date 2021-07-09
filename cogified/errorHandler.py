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
            print(error)
            return

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found, maybe you misspelled it?')
            print(error)
            return

        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('I am missing the required permissions.')
            print(error)
            return

        elif isinstance(error, commands.BadArgument):
            await ctx.send('Bad argument, maybe try doing it better next time?')
            print(error)
            return
        
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('This command is currently disabled.')
            print(error)
            return
        
        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send('Extension is already loaded.')
            print(error)
            return
        
        elif isinstance(error, commands.ExtensionError):
            await ctx.send('There was an error with the extension.')
            print(error)
            return
        
        elif isinstance(error, commands.ExtensionFailed):
            await ctx.send('The extension failed..maybe try again later.')
            print(error)
            return
        
        elif isinstance(error, commands.ExtensionNotFound):
            await ctx.send('Unknown extension, unable to find. TypeError?')
            print(error)
            return

        elif isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send('Extension not loaded, please load the extension first.')
            print(error)
            return
        
        elif isinstance(error, commands.MissingRole):
            await ctx.send('User is missing a certain role.')
            print(error)
            return
        
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the correct permissions to use this command.')
            print(error)
            return

        elif isinstance(error, commands.BotMissingRole):
            await ctx.send('I do not have the correct role to execute this command.')
            print(error)
            return
        
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('Can not find the member that was supplied.')
            print(error)
            return
        
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('Cannot private message the user.')
            print(error)
            return

        elif isinstance(error, commands.NotOwner):
            await ctx.send('You are not the creator of me, you cannot use this command.')
            print(error)
            return
        
        elif isinstance(error, commands.MessageNotFound):
            await ctx.send('Message was not found.')
            print(error)
            return
        
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send('Role not found, try again?')
            print(error)
            return
        
        elif isinstance(error, commands.UserNotFound):
            await ctx.send('User was not found.')
            print(error)
            return
        
        elif isinstance(error, commands.EmojiNotFound):
            await ctx.send('Emoji not found...what emoji are you looking for exactly?')
            print(error)
            return

        elif isinstance(error, commands.GuildNotFound):
            await ctx.send('Cannot find the guild.')
            print(error)
            return
        
        elif isinstance(error, commands.ChannelNotFound):
            await ctx.send('Channel was not found.')
            print(error)
            return
        
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send('There is an invoke error.')
            print(error)
            return
        
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send('Too many arguments, try again.')
            print(error)
            return
        
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)
            print(error)
            return

        else:

            raise error

def setup(client):
    client.add_cog(errorHandler(client))