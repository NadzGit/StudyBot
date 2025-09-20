# bot.py
import os
import asyncio

import discord
from dotenv import load_dotenv

#basic setup of bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD= os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event #sending dm to a member on join
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"heyyy {member.name} pooookieeeee :3")

    channel_id=1418226262677393512
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(f"HALLOO {member.mention}!") #mentioned in the channel on join
    else:
        print("Something went wrong.")




@client.event
async def on_message(message):
    if message.author == client.user or isinstance(message.channel, discord.TextChannel): #to prevent loops and to prevent timers being started in the Guild
        return
    start_timer = "Your time starts now love! You got this!!" 
    
    if "timer" in message.content.lower():
            await message.channel.send(start_timer)
    
    if message.author == client.user:
        return
    await asyncio.sleep(6)
    await message.author.send("Time up queen :3") #works for both dms and in server

    

    
# @client.command()
# async def pomodoro_message(ctx):
#     await asyncio.sleep (5)
#     await ctx.author.send("Time Up")


client.run(TOKEN)