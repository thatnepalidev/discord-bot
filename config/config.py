import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variables
TOKEN = os.getenv('BOT_TOKEN')