from bot.client import create_bot
from bot.config import TOKEN
from bot.commands import pomodoro
from bot.events import ready, members

bot = create_bot()

ready.setup(bot)
members.setup(bot)
pomodoro.setup(bot)

bot.run(TOKEN)