import discord

def setup(bot):
    @bot.tree.command(name="server", description="sends invite link to server")
    async def server(interaction : discord.Interaction):
        await interaction.response.send_message('https://discord.gg/UUu3r7DtAQ')