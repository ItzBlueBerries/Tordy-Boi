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

test = "hi"

color1 = "#8B0000"

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix, help_command=None)

################################### Cog Stuff Lol ###########################################

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogified.{extension}')
    await ctx.send(f'{extension} successfully loaded.')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogified.{extension}')
    await ctx.send(f'{extension} successfully unloaded.')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogified.{extension}')
    client.load_extension(f'cogified.{extension}')
    await ctx.send(f'{extension} successfully reloaded.')

for filename in os.listdir('./cogified'):
    if filename.endswith('.py'):
        client.load_extension(f'cogified.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))