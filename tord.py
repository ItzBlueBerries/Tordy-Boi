# Start of Tordy Boi Code lol 😎

#### Imports ####

import os
from dotenv import load_dotenv
import json
import discord
from discord.ext import commands
import random
from discord.guild import Guild

################ Start of stuff lol ################

load_dotenv()

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)

################### Events ##########################################

"""
@client.event
async def on_ready():
    print('Tordy is online, lol.')
"""

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "t!"

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4) 

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing arguments.')
        return
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Bad argument')
        return
    else:
        raise error

############################### Useless Shit ################################################################

## PING

"""
@client.command()
async def ping(ctx):
    await ctx.send('Pong! (Is this a testing command? :0 lol)')
"""

## 8BALL

""" This for later :)
@client.command(aliases=['8ball', '8b'])
async def eightball(ctx, *, question):
    responses = ['hi', 
                'testing command', 
                'this is just testing responses', 
                'lol',
                'honestly make remove this command after the test lol, for now.']
    await ctx.send(f'__***8ball Command***__\nQuestion: *{question}*\nAnswer: *{random.choice(responses)}*')
"""

############################## Moderation Mess. #############################################################

## KICK

@client.command(aliases=['boot'])
async def kick(ctx, member:discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.kick_members):
        await ctx.send('Yeah, you don\'t have the `KICK_MEMBERS` permission, lol.')
        return
    await member.kick(reason=reason)
    await ctx.send(f'***{member.mention}***, has been kicked successfully.\n(Check audit log for reason.)')

## BAN

@client.command(aliases=['hammer'])
async def ban(ctx, member:discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('Yeah, you don\'t have the `BAN_MEMBERS` permission, lol.')
        return
    await member.ban(reason=reason)
    await ctx.send(f'***{member.mention}***, has been banned successfully.\n(Check ban list for reason.)')

## UNBAN

@client.command(aliases=['forgive'])
async def unban(ctx, *, member):
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

## PURGE

@client.command(aliases=['clear', 'clean'])
async def purge(ctx, amount=11):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send('Yeah, you don\'t have the `MANAGE_MESSAGES` permission, lol.')
        return
    ammount = amount+1
    if amount > 101:
        await ctx.send('Over 100 messages?!?!? ARE YOU CRAZY??!?!?!?!?')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Purged Messages.')

## MUTE

@client.command()
async def mute(ctx, member:discord.Member, *, reason=None):
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

## UNMUTE

@client.command()
async def unmute(ctx, member:discord.Member, *, reason=None):
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

################################## Utility ################################

## SETPREFIX

@client.command(aliases=['prefix'])
async def setprefix(ctx, prefixset=None):
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

################################### Cog Stuff Lol ###########################################

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogified.{extension}')
    await ctx.send(f'{extension} successfully loaded.')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogified.{extension}')
    await ctx.send(f'{extension} successfully unloaded.')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogified.{extension}')
    client.load_extension(f'cogified.{extension}')
    await ctx.send(f'{extension} successfully reloaded.')

for filename in os.listdir('./cogified'):
    if filename.endswith('.py'):
        client.load_extension(f'cogified.{filename[:-3]}')

################################ Error Handling #############################################

"""
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required arguments...(`kick <@mention> [reason]`)')
        return
"""

client.run(os.getenv('DISCORD_TOKEN'))