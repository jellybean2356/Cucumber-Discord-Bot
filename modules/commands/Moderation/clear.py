import discord

def setup(bot):
    @bot.tree.command(name="clear", description="purge chat history")
    async def clear(interaction : discord.Interaction, amount : int):
        if amount > 300:
            await interaction.response.send_message("You cannot purge this many messages.", ephemeral=True)
            return
        
        if amount < 1:
            await interaction.response.send_message("You cannot purge this many messages.", ephemeral=True)
            return
        
        await interaction.response.send_message("Purging messages...", ephemeral=True)
        await interaction.channel.purge(limit=amount)
        await interaction.followup.send(f"Purged {amount} messages in the channel.", ephemeral=True)
