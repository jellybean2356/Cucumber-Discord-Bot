import discord
from discord.ext import commands
from config import DISCORD_BOT_TOKEN
from modules import load, database

# Bot config
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!cucumber', intents=intents)
bot.help_command = None
bot.activity = discord.Game(name="/help")

# Loading content to this file
load.commands(bot)
load.ai(bot)

# Functions that happen after the bot has been initialized
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    database.setup_db(bot)
    await bot.tree.sync()

# Run the bot
bot.run(DISCORD_BOT_TOKEN)