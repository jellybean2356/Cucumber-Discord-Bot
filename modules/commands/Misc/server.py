import discord

def setup(bot):
    @bot.tree.command(name="server", description="sends invite link to server")
    async def server(interaction : discord.Interaction):
        await interaction.response.send_message('https://discord.com/invite/96msqzQ6FR')