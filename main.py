import discord
from discord.ext import commands
import os
from bot_setup import bot
import moderation


# Load environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)