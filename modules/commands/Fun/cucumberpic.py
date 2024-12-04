import discord
import requests
import random
from config import SERPAPI_KEY

def setup(bot):
    @bot.tree.command(name="cucumberpic", description="sends random cucumber picture from internet")
    async def cucumberpic(interaction: discord.Interaction):
        search_params = {
            "engine": "google_images",
            "q": "cucumber",
            "hl": "en",
            "gl": "us",
            "tbs": "il:cl",
            "api_key": SERPAPI_KEY,
            "num": 100000,
            "start": random.randint(0, 100000), 
        }

        response = requests.get("https://serpapi.com/search", params=search_params)
        search_results = response.json()
        if "images_results" in search_results and len(search_results["images_results"]) > 0:
                    random_image = random.choice(search_results["images_results"])
                    image_url = random_image.get("thumbnail")
                    if image_url:
                        await interaction.response.send_message(image_url)
                        return
