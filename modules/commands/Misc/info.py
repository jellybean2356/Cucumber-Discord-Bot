import discord
import datetime
from config import CC_COLOR

start_time = datetime.datetime.utcnow()

def setup(bot):
    @bot.tree.command(name="info", description="shows bot info")
    async def info(interaction : discord.Interaction):
        bot_uptime = datetime.datetime.utcnow() - start_time
        bot_uptime_str = format_timedelta(bot_uptime)
        num_servers = len(bot.guilds)

        embed=discord.Embed(title='Bot informations', color=CC_COLOR)

        embed.add_field(name='bot uptime', value=bot_uptime_str, inline=False)
        embed.add_field(name='server count', value=num_servers, inline=False)

        await interaction.response.send_message(embed=embed)

def format_timedelta(delta):
    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{days}:{hours}:{minutes}:{seconds}"