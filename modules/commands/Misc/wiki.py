import discord
import wikipediaapi
from discord.ext import commands
from config import CC_COLOR

wiki_wiki = wikipediaapi.Wikipedia(user_agent='Cucumber/beta.3.0')

def setup(bot):
    @bot.tree.command(name="wiki", description="find things on wiki")
    async def wiki(interaction : discord.Interaction, query : str):
        page_py = wiki_wiki.page(query)
        if not page_py.exists():
            await interaction.response.send_message("no results found")
            return
        title = page_py.title
        sentences = page_py.summary.split('.')[:5]
        summary = '.'.join(sentences)
        summary_full = (summary + "...")
        embed = discord.Embed(
            title=title,
            description=summary_full,
            color=CC_COLOR
        )
        embed.add_field(name="read more: ", value=f"{page_py.fullurl}", inline=False)
        await interaction.response.send_message(embed=embed)