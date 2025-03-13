import random
import discord
import os
from discord import app_commands
from discord.ext import commands

DICE_IMAGES = {
    1: r"img\dice\1.png",
    2: r"img\dice\2.png",
    3: r"img\dice\3.png",
    4: r"img\dice\4.png",
    5: r"img\dice\5.png",
    6: r"img\dice\6.png",
}

async def setup(bot: commands.Bot):
    @bot.tree.command(name="dice", description="Roll a six-sided dice")
    async def dice_command(interaction: discord.Interaction):
        roll = random.randint(1, 6)
        
        # Get absolute path to the image
        image_path = os.path.join(os.path.dirname(__file__), '..', DICE_IMAGES[roll])
        
        embed = discord.Embed(title=f"You rolled a **{roll}**!", color=discord.Color.blue())
        # Use file upload for local image
        file = discord.File(image_path, filename=f"dice-{roll}.png")
        embed.set_image(url=f"attachment://dice-{roll}.png")
        
        await interaction.response.send_message(embed=embed, file=file)