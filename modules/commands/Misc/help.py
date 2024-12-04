import discord
from config import CC_COLOR

def setup(bot):
    @bot.tree.command(name="help", description="shows help screen")
    async def help(interaction : discord.Interaction):
        with open ('help_cmd.txt', 'r') as file:
            content = file.read()

        embed = discord.Embed(
            title='Help Menu',
            description=content,
            color=CC_COLOR
        )
        await interaction.response.send_message(embed=embed)