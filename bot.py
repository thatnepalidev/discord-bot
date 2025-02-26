import discord
from discord.ext import commands
from config.config import TOKEN
from events.on_ready import setup as setup_on_ready
from commands.random import setup as setup_random
from commands.quotes import setup as setup_quotes

# Create a bot instance with intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Setup events and commands
async def main():
    await setup_on_ready(bot)  # Await the setup coroutine for on_ready
    await setup_random(bot)    # Await the setup coroutine for random command
    await setup_quotes(bot)  # Await the setup coroutine for quotes command
    await bot.start(TOKEN)     # Start the bot

# Run the bot
import asyncio
asyncio.run(main())