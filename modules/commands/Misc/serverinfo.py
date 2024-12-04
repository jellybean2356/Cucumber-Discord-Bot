import discord
import os
import json
from config import CC_COLOR

def setup(bot):
    @bot.tree.command(name="serverinfo", description="obtain info about server")
    async def serverinfo(interaction : discord.Interaction):
        server = interaction.guild

        embed=discord.Embed(
            title=server.name + " stats",
            description=f"users: {server.member_count}\nserver id: {server.id}\ndisplay name: " + server.name,
            color=CC_COLOR
        )
        await interaction.response.send_message(embed=embed)