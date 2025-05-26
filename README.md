# #Tarot

A dope Discord bot for badass tarot reading.

![New Project (10)](https://github.com/user-attachments/assets/b5d505f5-e5d4-45bc-868b-91a0cea49877)

## Features
- `/one_card` – Single card reading  
- `/three_cards` – Past, present, and future reading  
- `/yes_no` – Yes or no answer to a question  

## Prerequisites
- Python 3.8 or higher  
- A Discord bot and its token (create one at [Discord Developer Portal](https://discord.com/developers/applications))

## Setup and Installation

1. **Clone the repository and navigate to the bot directory:**
   ```bash
   git clone https://github.com/thatnepalidev/discord-bot.git
   cd discord-bot/tarot
2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate

3. **Install the required packages:**

   ```bash
   pip install discord pillow python-dotenv

4. **Add your bot token to a .env file:**

   ```bash
   echo DISCORD_TOKEN=your_discord_bot_token_here > .env
   
   Or create .env manually and add:

   DISCORD_TOKEN=your_discord_bot_token_here

5. **Run the bot:**

   ```bash
   python main.py
