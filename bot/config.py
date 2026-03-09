import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#basic setup of bot
load_dotenv()
TOKEN= os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv("GUILD_ID").strip())
GUILD = os.getenv('DISCORD_GUILD')
WELCOME_CHANNEL_ID = os.getenv('WELCOME_CHANNEL_ID')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
client=commands.Bot(command_prefix="!", intents=intents)