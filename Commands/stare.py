import discord
from discord.ext import commands
import random

class Stare(commands.Cog):
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
    async def stare(self, ctx):
        """Stare at something"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099140258781724673/1099941233108983818/anime-naruto.gif",
                      "https://cdn.discordapp.com/attachments/1099140258781724673/1099941233515835422/anime-sword-art-online.gif",
                      "https://cdn.discordapp.com/attachments/1099140258781724673/1099941233931079752/anime-what.gif",
                      "https://cdn.discordapp.com/attachments/1099140258781724673/1099941234300166206/lamy-stare-anime-stare.gif",
                      "https://cdn.discordapp.com/attachments/1099140258781724673/1099941234698637312/maika-blend-s.gif",
                      "https://cdn.discordapp.com/attachments/1099140258781724673/1099941235105472603/nichijou-blank-stare.gif",
                      "https://cdn.discordapp.com/attachments/1099140258781724673/1099941235453603911/rin-anime.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} is staring at something.",
                   f"{ctx.author.display_name} is staring some body must have felt a chill.",
                   f"{ctx.author.display_name} is observing.",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
    await bot.add_cog(Stare(bot))