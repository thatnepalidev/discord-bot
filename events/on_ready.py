import discord
from discord.ext import commands

async def setup(bot: commands.Bot):
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')
        await bot.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Planting flowers 🌼"
            )
        )
        await bot.tree.sync()  # Sync commands with Discord
        print("Commands synced.")
