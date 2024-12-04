import discord
from config import CC_COLOR

def setup(bot):
   @bot.tree.command(name="credits", description="shows credits")
   async def credits(interaction : discord.Interaction):
      embed = discord.Embed(
         title='Credits Menu',
         description="""made by jellybean, Gupierre who send us a hell lot of juicy cucumber pictures, somebody9664 who created the idea for most of commands there. thanks for using the most goofy ahh bot whats on discord, go kill yourself :3""",
         color=CC_COLOR
      )
      await interaction.response.send_message(embed=embed)