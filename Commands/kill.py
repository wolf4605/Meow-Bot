import discord
from discord.ext import commands
import random



class Kill(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    #Just a Event to ensure the cog is loading
    @commands.Cog.listener()
    async def on_ready(self):
        print("______________")
    
    async def cog_load(self):
        print (f"{self.__class__.__name__} command has been loaded.")

    #The Command
    @commands.hybrid_command()
    async def kill(self, ctx:commands.context, member: discord.Member):
        """Kill a player"""
    # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097782406276190309/1098094079738392627/giphy.gif",
                    "https://cdn.discordapp.com/attachments/1097782406276190309/1098150399741014097/anime-wasted.gif",
                    "https://cdn.discordapp.com/attachments/1097782406276190309/1098151524976308224/anime-wasted_1.gif",
                    "https://cdn.discordapp.com/attachments/1097782406276190309/1098152404563787816/wasted-haikyuu.gif",
                    "https://cdn.discordapp.com/attachments/1097782406276190309/1098152562387071047/anime-girl.gif",
                    "https://cdn.discordapp.com/attachments/1097782406276190309/1098152867254239333/anime-wasted_2.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} completely obliterates {member.display_name} to death!",
                f"{ctx.author.display_name} brutally murders {member.display_name}!! 💀",
                f"{ctx.author.display_name} murdered {member.display_name}!!! Brutal",
                f"{ctx.author.display_name} eliminates {member.display_name} out of existence !!!",
                f"{ctx.author.display_name} annihilates {member.display_name} !! Poor them...",
                ]
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

    
async def setup(bot:commands.Bot):
    await bot.add_cog(Kill(bot))
