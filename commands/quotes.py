import random
import discord
from discord import app_commands
from discord.ext import commands

# Function to load quotes from the text file
def load_quotes(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

async def setup(bot: commands.Bot):
    @bot.tree.command(name="quotes", description="Get a random motivational quote")
    async def quotes_command(interaction: discord.Interaction):
        quotes = load_quotes("source/quotes.txt")  # Adjust path if needed
        random_quote = random.choice(quotes)
        await interaction.response.send_message(random_quote)