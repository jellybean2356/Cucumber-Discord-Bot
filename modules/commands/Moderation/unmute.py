import discord
from discord.ext import commands
import datetime

def setup(bot):
    @discord.app_commands.checks.has_permissions(mute_members=True)
    @discord.app_commands.AppCommandError
    async def error(interaction : discord.Interaction):
        await interaction.response.send_message('you dont have permissions to use this command')
    @bot.tree.command(name="unmute", description="unmute an user")
    async def unmute(interaction : discord.Interaction, member : discord.Member):
        try:
            delta = datetime.timedelta(seconds=0)
            await member.timeout(delta)
        except Exception as e:
            await interaction.response.send_message('you dont have permissions to mute this user')
            return
        await interaction.response.send_message('user ' + member.mention + ' has been unmuted')
