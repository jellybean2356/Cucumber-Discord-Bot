import random
import discord
from discord.ext import commands

def setup(bot):
    @bot.tree.command(name="coinflip", description="flip a coin")
    async def coinflip(interaction : discord.Interaction):
        result = random.choice(['head', 'tails'])
        await interaction.response.send_message(result)