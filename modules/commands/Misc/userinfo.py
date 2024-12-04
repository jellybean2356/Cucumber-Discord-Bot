import discord
from modules import database
from config import CC_COLOR

def setup(bot):
    @bot.tree.command(name="userinfo", description="obtain info about user")
    async def userinfo(interaction : discord.Interaction, user : discord.Member):
        guildid = interaction.guild_id
        userid = user.id

        embed = discord.Embed(
            title=(user.display_name + "'s stats"),
            description=f"warns: {database.get_user_warns(userid, guildid)}\n\ndisplay name: " + user.display_name + f"\nuserID: {user.id}\ndate of creation: " + str(user.created_at) + "\n ",
            color=CC_COLOR
        )
        avatar = user.display_avatar
        embed.set_image(url=avatar)

        await interaction.response.send_message(embed=embed)