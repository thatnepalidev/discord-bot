import discord
from discord import app_commands
from deep_translator import GoogleTranslator
from typing import List

LANGUAGES = {
    'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali',
    'ca': 'Catalan', 'cs': 'Czech', 'da': 'Danish', 'de': 'German',
    'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian',
    'fa': 'Persian', 'fi': 'Finnish', 'fr': 'French', 'gu': 'Gujarati',
    'he': 'Hebrew', 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian',
    'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
    'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian', 'mk': 'Macedonian',
    'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali', 'nl': 'Dutch',
    'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian',
    'ru': 'Russian', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali',
    'sq': 'Albanian', 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil',
    'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian',
    'ur': 'Urdu', 'vi': 'Vietnamese', 'zh': 'Chinese'
}

class Translate(app_commands.Group):
    def __init__(self):
        super().__init__(name="translate", description="Translate text between languages")
        
    @app_commands.command(name="text", description="Translate text to another language")
    @app_commands.describe(
        text="The text you want to translate",
        language="The target language to translate to"
    )
    async def translate(
        self,
        interaction: discord.Interaction,
        text: str,
        language: str
    ) -> None:
        await interaction.response.defer()
        
        try:
            # Convert full language name to code
            target_lang = None
            for code, name in LANGUAGES.items():
                if name.lower() == language.lower():
                    target_lang = code
                    break
            
            if not target_lang:
                await interaction.followup.send(
                    f"Invalid language. Please use one of: {', '.join(LANGUAGES.values())}",
                    ephemeral=True
                )
                return

            # Translate the text
            translator = GoogleTranslator(source='auto', target=target_lang)
            translated = translator.translate(text)
            
            # Create embed for response
            embed = discord.Embed(
                color=discord.Color.blue()
            )
            embed.add_field(name="Original Text", value=text, inline=False)
            embed.add_field(name=f"Translation to {LANGUAGES[target_lang]}", value=translated, inline=False)
            
            await interaction.followup.send(embed=embed)
            
        except Exception as e:
            await interaction.followup.send(
                f"An error occurred while translating: {str(e)}",
                ephemeral=True
            )

    @translate.autocomplete('language')
    async def language_autocomplete(
        self,
        interaction: discord.Interaction,
        current: str
    ) -> List[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=lang_name, value=lang_name)
            for lang_name in LANGUAGES.values()
            if current.lower() in lang_name.lower()
        ][:25]

async def setup(bot):
    bot.tree.add_command(Translate())