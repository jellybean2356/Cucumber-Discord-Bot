import discord
from discord.ext import commands
import datetime
from unidecode import unidecode


def setup(bot):
    @discord.app_commands.checks.has_permissions(mute_members=True)
    @discord.app_commands.AppCommandError
    async def error(interaction : discord.Interaction):
        await interaction.response.send_message('you dont have permissions to use this command')
    @bot.tree.command(name="mute", description="mute an user")
    async def mute(interaction : discord.Interaction, member : discord.Member, weeks : int = None, days : int = None, hours : int = None, minutes : int = None):
        if not weeks and not days and not hours and not minutes:
            await interaction.response.send_message('please enter for how much should the user be muted.')
            return
       
        if not weeks:
            weeks = 0
        if not days:
            days = 0
        if not hours:
            hours = 0
        if not minutes:
            minutes = 0
    
        delta_duration = datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes)
        try:
            await member.timeout(delta_duration)
        except Exception as e:
            await interaction.response.send_message('you dont have permissions to mute this user')
            return

        await interaction.response.send_message('user ' + member.mention + f' has been muted for {weeks}w {days}d {hours}h {minutes}m')
        


