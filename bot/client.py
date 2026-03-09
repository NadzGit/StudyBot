import discord
from discord.ext import commands

def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True 
    
    
    return commands.Bot(command_prefix="!", intents=intents)


    