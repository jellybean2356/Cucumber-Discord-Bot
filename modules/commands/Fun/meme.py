import discord
from discord.ext import commands
import requests

def setup(bot):
   @bot.tree.command(name="meme", description="get a random meme")
   async def meme(interaction : discord.Interaction, query : str):
      try:
         if not query:
            url = "https://meme-api.com/gimme"
            response = requests.get(url)
            meme_data = response.json()
            meme_url = meme_data['url']
            await interaction.response.send_message(meme_url)
         else:
            url = f"https://meme-api.com/gimme/{query}"
            response = requests.get(url)
            meme_data = response.json()
            meme_url = meme_data['url']
            await interaction.response.send_message(meme_url)
      except Exception as e:
         await interaction.response.send_message(f"meme named {query} couldnt be found anywhere.")