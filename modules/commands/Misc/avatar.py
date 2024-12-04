import discord

def setup(bot):
   @bot.tree.command(name="avatar", description="sends a avatar of an user")
   async def avatar(interaction : discord.Interaction, member : discord.Member):
      await interaction.response.send_message(f"{member.display_avatar}")