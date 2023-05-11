import discord
from discord.ext import commands
import random

class Pet(commands.Cog):
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
    async def pat(self, ctx, member: discord.Member):
        """Pet a Cutie"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097837608652001300/1098269282103730186/pat.gif",
                    "https://cdn.discordapp.com/attachments/1097837608652001300/1098269281663332382/pat_1.gif",
                    "https://cdn.discordapp.com/attachments/1097837608652001300/1098269281218727996/kanna-kamui-pat.gif",
                    "https://cdn.discordapp.com/attachments/1097837608652001300/1098269280874799234/horimiya-pat-pat-anime.gif",
                    "https://cdn.discordapp.com/attachments/1097837608652001300/1098269280421818419/emi-emilia.gif",
                    "https://cdn.discordapp.com/attachments/1097837608652001300/1098269280035938325/anime-pat.gif",
                    "https://cdn.discordapp.com/attachments/1097837608652001300/1098269279226441739/anime-pat_1.gif",
                    "https://cdn.discordapp.com/attachments/1097837608652001300/1098269278668595200/anime-good-girl.gif",
                    "https://cdn.discordapp.com/attachments/1097837608652001300/1098269278085582899/aharensan-aharen.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} is petting {member.display_name}",
                f"{member.display_name}, you have been patted by {ctx.author.display_name} !",
                f"{ctx.author.display_name} pats {member.display_name} gently",
                f"{ctx.author.display_name} pets {member.display_name}'s head ! Adorable ! 💕 ",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
    await bot.add_cog(Pet(bot))