import discord
from discord.ext import commands

async def setup(bot: commands.Bot):
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')
        await bot.tree.sync()  # Sync commands with Discord
        print("Commands synced.")