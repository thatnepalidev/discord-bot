import random
import discord
from discord import app_commands
from discord.ext import commands

async def setup(bot: commands.Bot):
    @bot.tree.command(name="random", description="Generate a random number between two numbers")
    async def random_command(interaction: discord.Interaction, initial: int, final: int):
        if initial > final:
            await interaction.response.send_message("The initial number must be less than the final number.")
            return
        
        random_number = random.randint(initial, final)
        await interaction.response.send_message(f'Your random number is {random_number}')