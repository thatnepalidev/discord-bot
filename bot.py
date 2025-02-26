import os
import random
import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Enable intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When bot is ready, sync commands
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user.name}')

# Slash command: /motivate
@bot.tree.command(name="motivate", description="Get a motivational quote!")
async def motivate(interaction: discord.Interaction):
    quotes = [
        "You got this! 💪",
        "Believe in yourself! 🌟",
        "Every small step counts! 🚶‍♂️",
        "You're doing great! Keep going! 🔥",
        "Success is a journey, not a destination. Keep moving forward! 🏆"
    ]
    await interaction.response.send_message(random.choice(quotes))

# Slash command: /remind
@bot.tree.command(name="remind", description="Set a reminder.")
async def remind(interaction: discord.Interaction, time: int, message: str):
    await interaction.response.send_message(f"Reminder set for {time} minutes: '{message}'")
    await asyncio.sleep(time * 60)
    await interaction.followup.send(f"⏰ Reminder: {message}")

# Slash command: /timer
@bot.tree.command(name="timer", description="Set a timer.")
async def timer(interaction: discord.Interaction, time: int):
    await interaction.response.send_message(f"Timer set for {time} minutes. ⏳")
    await asyncio.sleep(time * 60)
    await interaction.followup.send(f"⏰ Time's up! {time} minutes have passed.")

# Slash command: /push-ups
@bot.tree.command(name="push_ups", description="Challenge yourself with push-ups!")
async def push_ups(interaction: discord.Interaction, count: int):
    await interaction.response.send_message(f"Time for {count} push-ups! 💪")
    await asyncio.sleep(30)
    await interaction.followup.send(f"Great job! You've completed {count} push-ups! 🎉")

# Slash command: /random
@bot.tree.command(name="random", description="Generate a random number.")
async def random_cmd(interaction: discord.Interaction):
    random_number = random.randint(1, 100)
    await interaction.response.send_message(f"Your random number is: {random_number} 🎲")

# Run the bot
bot.run(TOKEN)
