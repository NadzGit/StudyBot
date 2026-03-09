from bot.config import WELCOME_CHANNEL_ID

def setup(bot):
    @bot.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(f"Hey! {member.name} Welcome to the Server! :3")

        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"HALLOO {member.mention}!")
        else:
            print("Something went wrong.")