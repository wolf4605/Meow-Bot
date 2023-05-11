import discord
from discord.ext import commands
import random

class Punch(commands.Cog):
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
    async def punch(self, ctx:commands.context, member: discord.Member):
        """Punch Some A**hole"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097837597298016286/1099942758296338452/anime-rezero.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942758690607144/anya-forger-damian-spy-x-family.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942759013548093/kimihito-monster-musume.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942759391051837/one-punch-man-saitama.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942759772717107/rimuru-rimuru-punch.gif",
                      "https://cdn.discordapp.com/attachments/1097837597298016286/1099942760141832242/rin243109-blue-exorcist.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} punched {member.display_name}!!! In you face 👊.",
                   f"{ctx.author.display_name} punched {member.display_name}!!! You can't see me 🖐️.",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
    await bot.add_cog(Punch(bot))