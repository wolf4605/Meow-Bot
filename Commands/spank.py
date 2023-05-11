import discord
from discord.ext import commands
import random


class Spank(commands.Cog):
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
    async def spank(self, ctx, member: discord.Member):
        """Spank a user"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097782168194912296/1098254998179151952/spank-bunny-naughty-bunny.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254997797490819/spank4.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254997487104080/spank.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254996933443735/spank_3.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254996023300229/spank_1.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254995645792296/rikka-takanashi-bad-girl.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254995289297016/bad-spank.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254994928578591/asobi-asobase-school-girl.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254994379112508/anime-school-girl.gif",
                    "https://cdn.discordapp.com/attachments/1097782168194912296/1098254993989054545/anime-girl.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} spanks {member.display_name} ! How naughty 〜",
                f"{ctx.author.display_name} spanks {member.display_name}'s butt !! Oh my 〜 !!",
                f"{ctx.author.display_name} spanked {member.display_name} 〜 kinky...",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
    await bot.add_cog(Spank(bot))