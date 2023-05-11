import discord
from discord.ext import commands
import random

class Poke(commands.Cog):
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
    async def poke(self, ctx, member: discord.Member):
        """Poke someone"""

        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099140487975276675/1099251937423138927/anime-poke.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251937813217371/anime-sleep.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251938215854081/boob-poke.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251938547212288/boop-anime.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251938886959115/poke_1.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251939251847249/poke_2.gif",
                      "https://cdn.discordapp.com/attachments/1099140487975276675/1099251939683876864/poke.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} poked {member.display_name}...",
                   f"{ctx.author.display_name} just poked {member.display_name}!!!"
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)
async def setup(bot:commands.Bot):
    await bot.add_cog(Poke(bot))