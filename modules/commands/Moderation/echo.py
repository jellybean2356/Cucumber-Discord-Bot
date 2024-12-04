import discord
from discord.ext import commands

def setup(bot):
    @discord.app_commands.checks.has_permissions(administrator=True)
    @discord.app_commands.AppCommandError
    async def error(interaction : discord.Interaction):
        await interaction.response.send_message('you dont have permissions to use this command')
    @bot.tree.command(name="echo", description="say a message")
    async def echo(interaction : discord.Interaction, message : str, channel : discord.TextChannel = None):
        if channel:
            await interaction.response.send_message('sent  message ***"' + message + '"***  to: ' + channel.mention, ephemeral=True)
            await channel.send(message)
        else:
            default_channel = interaction.channel
            await interaction.response.send_message('sent  message ***"' + message + '"***  to: ' + default_channel.mention, ephemeral=True)
            await default_channel.send(message)