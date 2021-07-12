import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['boot'])
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        if (not ctx.author.guild_permissions.kick_members):
            await ctx.send('Yeah, you don\'t have the `KICK_MEMBERS` permission, lol.')
            return
        await member.kick(reason=reason)
        await ctx.send(f'***{member.mention}***, has been kicked successfully.\n(Check audit log for reason.)')
    
    @commands.command(aliases=['hammer'])
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        if (not ctx.author.guild_permissions.ban_members):
            await ctx.send('Yeah, you don\'t have the `BAN_MEMBERS` permission, lol.')
            return
        await member.ban(reason=reason)
        await ctx.send(f'***{member.mention}***, has been banned successfully.\n(Check ban list for reason.)')

    @commands.command(aliases=['forgive'])
    async def unban(self, ctx, *, member):
        if (not ctx.author.guild_permissions.ban_members):
            await ctx.send('Yeah, you don\'t have the `BAN_MEMBERS` permission, lol.')
            return
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Forgive them? Okay well ***{user.mention}*** is now unbanned.')
                return

    @commands.command(aliases=['clear', 'clean'])
    async def purge(self, ctx, amount=11):
        if (not ctx.author.guild_permissions.manage_messages):
            await ctx.send('Yeah, you don\'t have the `MANAGE_MESSAGES` permission, lol.')
            return
        ammount = amount+1
        if amount > 101:
            await ctx.send('Over 100 messages?!?!? ARE YOU CRAZY??!?!?!?!?')
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send('Purged Messages.')

    @commands.command(aliases=['m'])
    async def mute(self, ctx, member:discord.Member, *, reason=None):
        if (not ctx.author.guild_permissions.manage_messages):
            await ctx.send('Yeah, you don\'t have the `MANAGE_MESSAGES` permission, lol.')
            return
        guild = ctx.guild
        muteRole = discord.utils.get(guild.roles, name="Muted")

        if not muteRole:
            await ctx.send('Man you guys don\'t make muted roles? Fine Ill make one, there.')
            muteRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(muteRole, speak=False, send_messages=False, read_messages_history=True, read_messages=True)
        await member.add_roles(muteRole, reason=reason)
        await ctx.send(f'{member.mention} has apparently been muted, lol.')
        await member.send(f'You have been muted in {guild.name}...you must have been bad.\nYou want the reason...?: ***{reason}***')

    @commands.command()
    async def unmute(self, ctx, member:discord.Member, *, reason=None):
        if (not ctx.author.guild_permissions.manage_messages):
            await ctx.send('Yeah, you don\'t have the `MANAGE_MESSAGES` permission, lol.')
            return
        guild = ctx.guild
        muteRole = discord.utils.get(guild.roles, name="Muted")

        if not muteRole:
            await ctx.send('Muted role has not been found, use the mute command to create it.')
            return

        await member.remove_roles(muteRole, reason=reason)
        await ctx.send(f'{member.mention} has apparently been unmuted, lol.')
        await member.send(f'You have been unmuted in {guild.name}...you must have been bad....BUT NOW YOUR GOOD!\nYou want the reason...?: ***{reason}***')

    @commands.command(aliases=['sm'])
    async def slowmode(self, ctx, time:int):
        if (not ctx.author.guild_permissions.manage_channels):
            await ctx.send('Yeah, you don\'t have the `MANAGE_CHANNELS` permission, lol.')
            return
        try:
            if time == 0:
                await ctx.send('Slowmode set to normal.')
                await ctx.channel.edit(slowmode_delay = 0)
            elif time > 21600:
                await ctx.send('Slowmode cannot go above 6 hours.')
                return
            else:
                await ctx.channel.edit(slowmode_delay = time)
                await ctx.send(f'Slowmode has been set: `{time} seconds`')
        except Exception:
            await ctx.send('...Error...I think..')
            await print('Huh...')
            return

    @commands.command()
    async def rename(self, ctx, arg1=None):
        if (not ctx.author.guild_permissions.manage_channels):
            await ctx.send('Yeah, you don\'t have the `MANAGE_CHANNELS` permission, lol.')
            return
        if arg1 == None:
            return await ctx.send('Must supply a channel to rename..')
        
        await ctx.message.channel.edit(name=arg1)
        await ctx.send('Renaming..')
        await asyncio.sleep(1)
        await ctx.send(f'Channel renamed to {arg1}')

    @commands.command()
    async def create(self, ctx, arg1=None):
        if (not ctx.author.guild_permissions.manage_channels):
            await ctx.send('Yeah, you don\'t have the `MANAGE_CHANNELS` permission, lol.')
            return
        if arg1 == None:
            return await ctx.send('Must supply a channel to create..')
        
        await ctx.guild.create_text_channel(arg1)
        await ctx.send('Creating..')
        await asyncio.sleep(1)
        await ctx.send(f'{arg1} has been created.')

def setup(client):
    client.add_cog(Moderation(client))