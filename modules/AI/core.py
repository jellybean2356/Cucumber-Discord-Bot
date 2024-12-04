from modules import database
import asyncio

from modules.AI import gemini, stabledif

def setup(bot):
    @bot.event
    async def on_message(message):
        if message.author.bot:
            return

        response = gemini.get_model_response(message)

        if "IMAGE GENERATION:" in response:
            asyncio.create_task(stabledif.SendImage(response, message.channel))
        else:
            asyncio.create_task(gemini.SendText(response, message.channel))

        database.update_channel_history(message, response)
        await bot.process_commands(message)