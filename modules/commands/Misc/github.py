import discord
from config import CC_COLOR

def setup(bot):
    @bot.tree.command(name="github", description="sends link to github repo")
    async def github(interaction : discord.Interaction):
        github = discord.Embed(
            title='Github Repo',
            description='https://github.com/jellybean2356/Cucumber-Discord-Bot',
            color=CC_COLOR
        )

        await interaction.response.send_message(embed=github)