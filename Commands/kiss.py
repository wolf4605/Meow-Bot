import discord
from discord.ext import commands
import random

class Kiss(commands.Cog):
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
    async def kiss(self, ctx, member: discord.Member):
        """You are smart enough to know what this does"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1099221779165237258/1099221982672863303/anime-kiss_1.gif",
                      "https://cdn.discordapp.com/attachments/1099221779165237258/1099221983201349683/anime-kiss.gif",
                      "https://cdn.discordapp.com/attachments/1099221779165237258/1099221983587217448/engage-kiss-anime-kiss.gif",
                      "https://cdn.discordapp.com/attachments/1099221779165237258/1099221983994069032/kiss.gif",
                      "https://cdn.discordapp.com/attachments/1099221779165237258/1099221984434475008/kiss-love.gif",
                      "https://cdn.discordapp.com/attachments/1099221779165237258/1099221984845508658/nagumi-koushi-hozumi-serene.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} kisses {member.display_name} ～ 💖 ",
                f"{ctx.author.display_name} smooches {member.display_name} !! How cute～",
                f"{ctx.author.display_name} kisses {member.display_name}!! Muwaaah",
                f"{ctx.author.display_name} kisses {member.display_name}!!! Things are heating up...",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
    await bot.add_cog(Kiss(bot))