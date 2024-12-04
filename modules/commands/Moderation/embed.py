import discord
from discord.ext import commands
from config import CC_COLOR

def setup(bot):
    @discord.app_commands.checks.has_permissions(administrator=True)
    @discord.app_commands.AppCommandError
    async def error(interaction : discord.Interaction):
        await interaction.response.send_message('you dont have permissions to use this command')
    @bot.tree.command(name="embed", description="send embed")
    async def embed(interaction : discord.Interaction, title : str, description : str, imageurl : str = None, channel : discord.TextChannel = None):
        embed=discord.Embed(
            title=title,
            description=description,
            color=CC_COLOR
        )

        if imageurl:
            embed.set_image(url=imageurl)
        if channel:
            await channel.send(embed=embed)
            await interaction.response.send_message('sent embed in: ' + channel.mention, ephemeral=True)
        else:
            await interaction.channel.send(embed=embed)
            await interaction.response.send_message('sent embed in: ' + interaction.channel.mention, ephemeral=True)