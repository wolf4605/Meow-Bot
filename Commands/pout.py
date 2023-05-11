import discord
from discord.ext import commands
import random

class Pout(commands.Cog):
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
    async def pout(self, ctx):
        """The name says it all"""

        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099140243724177579/1099255409933549589/noela-angry.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255409581236256/cute-pouting.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255409216344136/anime-fan27-pout.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255411061817406/pouts-pout.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255410671755294/pouting-angry.gif",
                      "https://cdn.discordapp.com/attachments/1099140243724177579/1099255410336223283/pout-anime.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} just pouted!!! awww~~~😊",
                   f"{ctx.author.display_name} pouted~~Kawaii~~"
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)
async def setup(bot:commands.Bot):
    await bot.add_cog(Pout(bot))