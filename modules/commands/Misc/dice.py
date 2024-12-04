import random
import discord

def setup(bot):
    @bot.tree.command(name="dice", description="throw a dice")
    async def dice(interaction : discord.Interaction):
        number = random.randint(1, 6)
        await interaction.response.send_message(number)
