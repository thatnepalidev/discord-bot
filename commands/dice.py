import random
import discord
from discord import app_commands
from discord.ext import commands

# Dictionary mapping dice rolls to image URLs
DICE_IMAGES = {
    1: "https://cdn-icons-png.flaticon.com/512/8336/8336943.png",
    2: "https://cdn-icons-png.flaticon.com/512/8336/8336956.png",
    3: "https://cdn-icons-png.flaticon.com/512/8336/8336955.png",
    4: "https://cdn-icons-png.flaticon.com/512/8336/8336933.png",
    5: "https://cdn-icons-png.flaticon.com/512/8336/8336931.png",
    6: "https://cdn-icons-png.flaticon.com/512/8336/8336948.png",
}

async def setup(bot: commands.Bot):
    @bot.tree.command(name="dice", description="Roll a six-sided dice")
    async def dice_command(interaction: discord.Interaction):
        roll = random.randint(1, 6)
        
        embed = discord.Embed(title=f"You rolled a **{roll}**!", color=discord.Color.red())
        embed.set_image(url=DICE_IMAGES[roll])
        
        await interaction.response.send_message(embed=embed)
