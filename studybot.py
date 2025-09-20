# bot.py
import os

import discord
from dotenv import load_dotenv

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




@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"heyyy {member.name} pooookieeeee :3")

    channel_id=1418226262677393512
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(f"HALLOO {member.mention}!")
    else:
        print("Something went wrong.")


client.run(TOKEN)
