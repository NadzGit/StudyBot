from bot.config import GUILD


def setup(bot):
    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')

        
        for guild in bot.guilds:
            if guild.name == GUILD:
                break
        print(
            f'{bot.user} is connected to the following guild:\n'
        
            f'{guild.name}(id: {guild.id})'
        )

