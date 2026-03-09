import discord
from bot.views.pomodoro_view import PomodoroView



def setup(bot):
# client.command()
    @bot.command()
    async def pomodoro(ctx):
        if ctx.author == bot.user: #to prevents bot responding to itself 
            return
        await ctx.send("Pick your study time ",view=PomodoroView())


#  if ctx.author == bot.user or isinstance(ctx.channel, discord.TextChannel): # replace above if statement with this condition if you want to keep timers within DMs