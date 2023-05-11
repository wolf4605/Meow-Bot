import discord
from discord.ext import commands
import random

class Laugh(commands.Cog):
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
    async def laugh(self, ctx, member: discord.Member):

        """Laugh at someone."""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097782632139468842/1098181103271022613/emilia-re-zero.gif",
                    "https://cdn.discordapp.com/attachments/1097782632139468842/1098181103761772624/fairy-tail-natsu.gif",
                    "https://cdn.discordapp.com/attachments/1097782632139468842/1098181104210546718/laugh-anime_1.gif",
                    "https://cdn.discordapp.com/attachments/1097782632139468842/1098181104588050452/laugh-anime.gif",
                    "https://cdn.discordapp.com/attachments/1097782632139468842/1098181105074573392/laugh-giggle.gif",
                    "https://cdn.discordapp.com/attachments/1097782632139468842/1098181105590485075/laughing-lol.gif",
                    "https://cdn.discordapp.com/attachments/1097782632139468842/1098181106051862528/nichijou-hahaha.gif",
                    "https://cdn.discordapp.com/attachments/1097782632139468842/1098181106362224641/rezero-rem.gif",
                    "https://cdn.discordapp.com/attachments/1097782632139468842/1098181106714558494/tomoko-kuroki.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} giggles at {member.display_name} !!!",
                f"{ctx.author.display_name} is laughing at {member.display_name} 😂 ",
                f"{ctx.author.display_name} finds {member.display_name} quite hilarious! ",
                f"{ctx.author.display_name} is rolling on the floor laughing at {member.display_name}!!! 🤣 ",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
    await bot.add_cog(Laugh(bot))