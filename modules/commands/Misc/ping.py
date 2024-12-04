import discord
import time

def setup(bot):
    @bot.tree.command(name="ping", description="shows cucumber's latency")
    async def ping(interaction : discord.Interaction):
        latency = round(bot.latency*1000)
        latency_value = str(latency)
        await interaction.response.send_message('pong!... ' + latency_value + ' ms')