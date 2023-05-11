import discord
from discord.ext import commands
import random

class RIP(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    #Just a Event to ensure the cog is loading
    @commands.Cog.listener()
    async def on_ready(self):
        print("______________")
    
    async def cog_load(self):
        print (f"{self.__class__.__name__} command has been loaded.")

    # The Command
    @commands.hybrid_command()
    async def rip(self, ctx):
        """Commit Sucide"""

        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097839574870405164/1099215525537656892/anime-alone.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215525881581598/anime-emotionless.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215526242299934/exhausted-tired.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215526636560434/falling-over.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215526988877834/kanokari-anime-fall.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215527412510814/reina-aharen-aharen-san-wa-hakarenai.gif",
                      "https://cdn.discordapp.com/attachments/1097839574870405164/1099215527743852544/suicide.gif",
                     ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} died a lonely death 💀",
                   f"{ctx.author.display_name}... 🪦 RIP",
                   f"May {ctx.author.display_name} rest peacefully",
                   f"{ctx.author.display_name} died!! One more weight off this world 💀",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)
async def setup(bot:commands.Bot):
    await bot.add_cog(RIP(bot))