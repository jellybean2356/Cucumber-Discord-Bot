import discord

def setup(bot):
    @bot.tree.command(name="cucumber", description="says the most shocking thing ever")
    async def cucumber(interaction : discord.Interaction):
        await interaction.response.send_message('cucumber!')