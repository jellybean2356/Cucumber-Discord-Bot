import discord
from discord.ext import commands
import praw
import asyncpraw
from config import CC_COLOR, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET

def setup(bot):
    @bot.tree.command(name="reddit", description="search subreddits")
    async def reddit(interaction : discord.Interaction, redditname : str, posts : int):
        try:
            if posts == 1:
                response_title = f"**Top 1 Post in r/{redditname}:**"
            else:
                response_title = f"**Top {posts} Hot Posts in r/{redditname}:**"
        
            response_embed = discord.Embed(
                title=response_title,
                color=CC_COLOR
            )
                
            reddit = praw.Reddit(client_id='IyADVNYGjGvCEydJOTTxWQ',
                        client_secret='9lg1jP0d65PDWpCKoeBcBcSz-GtPRw',
                        user_agent='cucumber/3.0')
        
            subreddit = reddit.subreddit(redditname)
            posts = subreddit.hot(limit=posts)
    
            for post in posts:
                    response_embed.add_field(name=post.title, value=post.url, inline=False)

            await interaction.response.send_message(embed=response_embed)

        except Exception as e:
            await interaction.response.send_message(f"Error: {e}")