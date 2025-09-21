import asyncio
import os
import discord
from discord.ui import Button
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


#basic setup of bot
load_dotenv()
TOKEN= os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv("GUILD_ID").strip())
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
client=commands.Bot(command_prefix="/", intents=intents)


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


def make_sleep():
    async def sleep(delay, result=None):
            coro = asyncio.sleep(delay, result=result)
            task = asyncio.ensure_future(coro)
            sleep.tasks.add(task)
            try:
                return await task
            except asyncio.CancelledError:
                return result
            finally:
                sleep.tasks.remove(task)

    sleep.tasks = set()
    sleep.cancel_all = lambda: sum(task.cancel() for task in sleep.tasks)
    return sleep

class Buttons(discord.ui.View):
    
    def disable_all_items(self):  #disabled both buttons after one is clicked
        for item in self.children:
            if isinstance(item, discord.ui.Button) and item.label != "Cancel Timer":
                item.disabled = True

   
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    #button 25
    @discord.ui.button(label="25 Minutes",style=discord.ButtonStyle.gray)
    async def grey_button(self,interaction:discord.Interaction,button:discord.Button,):
        self.disable_all_items()
        await interaction.response.edit_message(view=self)
        await interaction.user.send("25 mins start now")
        await sleep(5)
        await interaction.user.send(content="Time up queen :3")  
   
    #buttton 50
    @discord.ui.button(label="50 Minutes", style =discord.ButtonStyle.blurple)
    async def blurple_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        self.disable_all_items()
        await interaction.user.send("50 mins start now")
        await sleep(10)
        await interaction.followup.send(content = "Time up queen :3")  
    
    #cancel button + stop timers
    @discord.ui.button(label="Cancel Timer", style =discord.ButtonStyle.red)
    async def cancel_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        button.disabled = True   #diables button after pressed
        await interaction.response.edit_message(view=self)
        sleep.cancel_all()  #cancels running timers
        if sleep.tasks:
            await asyncio.wait(sleep.tasks)
        await interaction.user.send("You cancelled the timer booooooo loser")
     
        

@client.command()
async def pomodoro(ctx):
    if ctx.author == client.user or isinstance(ctx.channel, discord.TextChannel): #to prevents bot responding to itself and to prevent timers being started in the Guild
        return
    await ctx.send("Pick your study time ",view=Buttons())
    
    
sleep = make_sleep()


client.run(TOKEN)

