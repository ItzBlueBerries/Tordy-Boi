# Start of Tordy Boi Code lol 😎

#### Imports ####

from math import factorial
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

###################### Currency Functions ############################

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 150

    with open('bank.json', 'w') as f:
        json.dump(users, f, indent=4)
    return True

async def get_bank_data():
    with open('bank.json', 'r') as f:
        users = json.load(f)

    return users

async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('bank.json', 'w') as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]['bank']]
    return bal

################## Currency commands but I can't get cogs working right now lol #################################S

# BALANCE

@client.command(aliases=['bal'])
async def balance(ctx, member : discord.Member = None):
    if not member:
        member = ctx.author
    await open_account(member)

    users = await get_bank_data()
    user = member

    wallet_amount =  users[str(user.id)]["wallet"]
    bank_amount =  users[str(user.id)]["bank"]

    await ctx.send(
        f'__***{member.name}\'s Balance***__\n\n**Wallet:** *{wallet_amount}*\n**Bank:** *{bank_amount}*'
    )

# BEG

@client.command()
@commands.cooldown(1, 17, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()
    user = ctx.author

    earnings = random.randrange(310)

    people = [
        'Mr. Goodman',
        'Fruitsy',
        'Tordy Boi',
        'Dr. Phobia',
        'Katie Perry',
        'Tallie',
        'Drey',
	    'Kailani',	
        'Dewey',
	    'Rochella',	
        'Danyon',
	    'Trixibelle',	
        'Jetaime',
        'Daddy~',
        'Discord',
        'Tom',
        'Edd',
        'Matt'
    ]

    await ctx.send(f'**{random.choice(people)}** has given you: *{earnings}* coins/money.')

    users[str(user.id)]["wallet"] += earnings

    with open("bank.json", 'w') as f:
        json.dump(users, f, indent=4)

# WITHDRAW

@client.command(aliases=['with', 'wd', 'draw'])
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send('You did not provide an amount to withdraw.')
        return
    
    bal = await update_bank(ctx.author)

    if amount == "all":
        amount = bal[1]
    elif amount == "max":
        amount = bal[1]

    amount = int(amount)

    if amount < 0:
        await ctx.send('Amount given must be more then 0.')
        return
    
    if amount > bal[1]:
        await ctx.send('You do not have enough money to withdraw.')
        return

    await update_bank(ctx.author, amount, "wallet")
    await update_bank(ctx.author, -1*amount, "bank")

    await ctx.send(f'You withdrawed {amount}, are you satisfied yet? lol.')

@client.command(aliases=['depo'])
async def deposit(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send('You did not provide an amount to deposit.')
        return
    
    bal = await update_bank(ctx.author)

    if amount == "all":
        amount = bal[1]
    elif amount == "max":
        amount = bal[1]

    amount = int(amount)

    if amount < 0:
        await ctx.send('Amount given must be more then 0.')
        return
    
    if amount > bal[1]:
        await ctx.send('You do not have enough money to withdraw.')
        return

    await update_bank(ctx.author, -1*amount, "wallet")
    await update_bank(ctx.author, amount, "bank")

    await ctx.send(f'You deposited {amount}, are you satisfied yet? lol.')

@client.command(aliases=['dep', 'd', 'posit'])
async def give(ctx, member:discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send('You did not provide an amount to give.')
        return
    
    bal = await update_bank(ctx.author)

    if amount == "all":
        amount = bal[1]
    elif amount == "max":
        amount = bal[1]

    amount = int(amount)

    if amount < 0:
        await ctx.send('Amount given must be more then 0.')
        return
    
    if amount > bal[1]:
        await ctx.send('You do not have enough money to withdraw.')
        return

    await update_bank(ctx.author, -1*amount, "wallet")
    await update_bank(member, amount, "wallet")

    await ctx.send(f'You gave {member} {amount}, are you satisfied yet? lol.')

client.run(os.getenv('DISCORD_TOKEN'))