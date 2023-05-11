import discord
from discord.ext import commands
import random

class Kick(commands.Cog):
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
    async def kick(self, ctx, member: discord.Member):
        """Kick someone's balls if they have any"""
        # list of image URLs
        image_urls = ["https://cdn.discordapp.com/attachments/1097833659463118908/1098186462622666853/anime-dress.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186462933033040/anime-imouto.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186463432147026/emilia-fight.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186463981621318/kick.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186464531062784/kick-anime.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186465034371093/kick-in-the-balls-anime.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186465546096730/penitencia-kick.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186465986486282/shida-midori-midori.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186466443657226/taiga-aisaka-starling-bg-waifu.gif",
                    "https://cdn.discordapp.com/attachments/1097833659463118908/1098186466988937227/voz-dap-chym-dap-chym.gif",
                    ]
        # randomly select an image URL from the list
        image_url = random.choice(image_urls)

        phrases = [f"{ctx.author.display_name} lands a perfect kick at {member.display_name}, looks painful",
                f"{ctx.author.display_name} slam kicks {member.display_name}!! Ouch...",
                f"Watch out, {ctx.author.display_name} is kicking {member.display_name}!!!",
                f"{ctx.author.display_name} kicks {member.display_name}!",
                ]
        
        phrase = random.choice(phrases)
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.set_author(name=phrase,
                        icon_url=ctx.author.display_avatar)

        embed.set_image(url=image_url)
        # send the embed as a reply
        await ctx.send(embed=embed)

async def setup(bot:commands.Bot):
    await bot.add_cog(Kick(bot))