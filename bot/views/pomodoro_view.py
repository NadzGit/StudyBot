import asyncio
import discord
from bot.utils.sleep_manager import sleep

class PomodoroView(discord.ui.View):
    def disable_all_items(self):  #disabled both buttons after one is clicked
        for item in self.children:
            if isinstance(item, discord.ui.Button) and item.label != "Cancel Timer":
                item.disabled = True
               
   
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
        self.timer_task = None  # Holds the running timer task

    
    async def start_timer(self, interaction: discord.Interaction, minutes: int):
        await interaction.response.edit_message(view=self)
        await interaction.user.send(f"Your {minutes} minutes start now.")

        async def run_timer():
            await sleep(minutes * 60)
            await interaction.user.send("Your time is up!")
        
        self.timer_task = asyncio.create_task(run_timer())

    #button 25
    @discord.ui.button(label="25 Minutes", style=discord.ButtonStyle.gray)
    async def grey_button(self, interaction: discord.Interaction, button: discord.Button):
        self.disable_all_items()
        await self.start_timer(interaction, 25)
   

    @discord.ui.button(label="50 Minutes", style=discord.ButtonStyle.blurple)
    async def blurple_button(self, interaction: discord.Interaction, button: discord.Button):
        self.disable_all_items()
        await self.start_timer(interaction, 50)
    
    @discord.ui.button(label="Cancel Timer", style=discord.ButtonStyle.red)
    async def cancel_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        self.disable_all_items()
        await interaction.response.edit_message(view=self)

        if self.timer_task and not self.timer_task.done():
            self.timer_task.cancel()
            try:
                await self.timer_task
            except asyncio.CancelledError:
                pass
        await interaction.user.send("You cancelled the timer.")
