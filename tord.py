# Start of Tordy Boi Code lol 😎

#### Imports ####

from math import factorial
import os
from discord.user import Profile
from dotenv import load_dotenv
import json
import discord
from discord.ext import commands, tasks
import random
from discord.guild import Guild
import asyncio
import glob

################ Start of stuff lol ################

load_dotenv()

test = "hi"

color1 = "#8B0000"

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix, help_command=None)

################### Background Tasks Lol ####################3

async def ch_pr():
    await client.wait_until_ready()

    my_statuses = [f'Death? ... | t!help | {len(client.guilds)} servers.', f'Hi..I\'m tord.. | t!help | {len(client.guilds)} servers.']


    while not client.is_closed():

        status = random.choice(my_statuses)

        await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=status))

        await asyncio.sleep(15)

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

# async def open_account(user):
#     users = await get_bank_data()

#     if str(user.id) in users:
#         return False
#     else:
#         users[str(user.id)] = {}
#         users[str(user.id)]["wallet"] = 0
#         users[str(user.id)]["bank"] = 150

#     with open('bank.json', 'w') as f:
#         json.dump(users, f, indent=4)
#     return True

# async def get_bank_data():
#     with open('bank.json', 'r') as f:
#         users = json.load(f)

#     return users

# async def update_bank(user, change=0, mode="wallet"):
#     users = await get_bank_data()

#     users[str(user.id)][mode] += change

#     with open('bank.json', 'w') as f:
#         json.dump(users, f, indent=4)

#     bal = [users[str(user.id)]["wallet"], users[str(user.id)]['bank']]
#     return bal

# ################## Currency commands but I can't get cogs working right now lol #################################S

# # BALANCE

# @client.command(aliases=['bal'])
# async def balance(ctx, member : discord.Member = None):
#     if not member:
#         member = ctx.author
#     await open_account(member)

#     users = await get_bank_data()
#     user = member

#     wallet_amount =  users[str(user.id)]["wallet"]
#     bank_amount =  users[str(user.id)]["bank"]

#     await ctx.send(
#         f'__***{member.name}\'s Balance***__\n\n**Wallet:** *{wallet_amount}*\n**Bank:** *{bank_amount}*'
#     )

# # BEG

# @client.command()
# @commands.cooldown(1, 17, commands.BucketType.user)
# async def beg(ctx):
#     await open_account(ctx.author)

#     users = await get_bank_data()
#     user = ctx.author

#     earnings = random.randrange(310)

#     people = [
#         'Mr. Goodman',
#         'Fruitsy',
#         'Tordy Boi',
#         'Dr. Phobia',
#         'Katie Perry',
#         'Tallie',
#         'Drey',
# 	    'Kailani',	
#         'Dewey',
# 	    'Rochella',	
#         'Danyon',
# 	    'Trixibelle',	
#         'Jetaime',
#         'Daddy~',
#         'Discord',
#         'Tom',
#         'Edd',
#         'Matt',
#         'Popstar Jamie',
#         'TKOF',
#         'Blaze',
#         'Patrick',
#         'Spongebob',
#         'Squidward',
#         'Sandy',
#         'Mr. Krabs',
#         'Deimos',
#         'Hank',
#         'Tricky',
#         'Rule 34 Artist'
#     ]

#     await ctx.send(f'**{random.choice(people)}**, has given you: *{earnings}* *coins/money, satisfied yet?*')

#     users[str(user.id)]["wallet"] += earnings

#     with open("bank.json", 'w') as f:
#         json.dump(users, f, indent=4)

# # WITHDRAW

# @client.command(aliases=['with', 'wd', 'draw'])
# async def withdraw(ctx, amount=None):
#     await open_account(ctx.author)

#     if amount == None:
#         await ctx.send('You did not provide an amount to withdraw.')
#         return
    
#     bal = await update_bank(ctx.author)

#     if amount == "all":
#         amount = bal[0]
#     elif amount == "max":
#         amount = bal[0]

#     amount = int(amount)

#     if amount < 0:
#         await ctx.send('Amount given must be more then 0.')
#         return
    
#     if amount > bal[1]:
#         await ctx.send('You do not have enough money to withdraw.')
#         return

#     await update_bank(ctx.author, amount, "wallet")
#     await update_bank(ctx.author, -1*amount, "bank")

#     await ctx.send(f'You withdrawed {amount}, are you satisfied yet? lol.')

# @client.command(aliases=['depo'])
# async def deposit(ctx, amount=None):
#     await open_account(ctx.author)

#     if amount == None:
#         await ctx.send('You did not provide an amount to deposit.')
#         return
    
#     bal = await update_bank(ctx.author)

#     if amount == "all":
#         amount = bal[1]
#     elif amount == "max":
#         amount = bal[1]

#     amount = int(amount)

#     if amount < 0:
#         await ctx.send('Amount given must be more then 0.')
#         return
    
#     if amount > bal[1]:
#         await ctx.send('You do not have enough money to withdraw.')
#         return

#     await update_bank(ctx.author, -1*amount, "wallet")
#     await update_bank(ctx.author, amount, "bank")

#     await ctx.send(f'You deposited {amount}, are you satisfied yet? lol.')

# @client.command(aliases=['dep', 'd', 'posit'])
# async def give(ctx, member:discord.Member, amount=None):
#     await open_account(ctx.author)
#     await open_account(member)

#     if amount == None:
#         await ctx.send('You did not provide an amount to give.')
#         return
    
#     bal = await update_bank(ctx.author)

#     if amount == "all":
#         amount = bal[1]
#     elif amount == "max":
#         amount = bal[1]

#     amount = int(amount)

#     if amount < 0:
#         await ctx.send('Amount given must be more then 0.')
#         return
    
#     if amount > bal[1]:
#         await ctx.send('You do not have enough money to withdraw.')
#         return

#     await update_bank(ctx.author, -1*amount, "wallet")
#     await update_bank(member, amount, "wallet")

#     await ctx.send(f'You gave {member} {amount}, are you satisfied yet? lol.')

# # ROB

# @client.command(aliases=['steal'])
# async def rob(ctx, member : discord.Member = None):
#     if member == None:
#         await ctx.send('No member provided to rob..Please supply one.')
#         return

#     await open_account(ctx.author)
#     await open_account(member)

#     bal = await update_bank(member)
#     robberBal = await update_bank(ctx.author)

#     if robberBal[0] < 150:
#         return await ctx.send('You do not have atleast 150 coins to rob..')
#     else:
#         if bal[0] < 150:
#             return await ctx.send('Mentioned user does not have atleast 150 coins.')

#     stolen = random.randrange(-1*(robberBal[0]), bal[0])

#     await update_bank(ctx.author, stolen)
#     await update_bank(member,-1* stolen)

#     if stolen > 0:
#         return await ctx.send(f'You have took {stolen} coins...what a bad boy..🤣😂')
#     elif stolen < 0:
#         stolen = stolen*-1
#         return await ctx.send(f'You got caught stealing...what a bad boy, aren\'t you? lol.\nYou also paided {stolen} coins.')

# @client.command(aliases=['bet'])
# async def slots(ctx, amount=None):
#     if amount == None:
#         return await ctx.send('You can\'t bet air..')
    
#     await open_account(ctx.author)

#     bal = await update_bank(ctx.author)

#     amount = int(amount)

#     if amount < 100:
#         return await ctx.send('The minimum money to bet is 100..')
#     else:
#         if amount > bal[0]:
#             return await ctx.send('You do not have this much money...')

#         if amount < 0:
#             return await ctx.send('Amount needs be larger then 0..please..')

#     final = []
#     choice = ["🍎", "🍌", "🍉", "🎂", "💖", "🐍"]
#     for i in range(3):
#         a = random.choice(choice)

#         final.append(a)

#     await ctx.send(f'**Slots Game [{ctx.author.mention}]**\n**S L O T S**\n' + str(final))

#     if final[0] == final[1] == final[2]:
#         await update_bank(ctx.author, 3*amount)
#         await ctx.send('You got all 3 slots...hm, pretty good..check your balance.')
#     elif final[0] == final[1] or final[0] == final[2] or final[1] == final[2]:
#         await update_bank(ctx.author, 2*amount)
#         await ctx.send('You got 2 slots, good enough.')
#     else:
#         await update_bank(ctx.author,-1*amount, "wallet")
#         await ctx.send('All the slots man? That sucks.')

client.loop.create_task(ch_pr())

client.run(os.getenv('DISCORD_TOKEN'))