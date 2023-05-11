import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, Font, load_image
import random


class Wanted(commands.Cog):
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
    async def wanted(self, ctx, member: discord.Member, reward="10,000,000"):
        """Create a wanted poster of someone"""
        background = Editor("wanted.jpg")
        profile_image = load_image(str(member.display_avatar))
        profile = Editor(profile_image).resize((330, 340))
        run = Font("rundeck.ttf", size=40)
        run = Font("rundeck.ttf", size=35)
        
        background.paste(profile, (137, 253))
        background.rectangle(
            (137, 253),
            330,
            340,
            outline="black",
            stroke_width=8,
        )

        background.text(
            (300, 630),
            f"Name:  {member.display_name}",
            color="black",
            font=run,
            align="center",
        )

        background.text(
            (300, 720),
            f"Guild: {member.guild.name}",
            color="black",
            font=run,
            align="center",
        )

        background.text(
            (300, 815),
            f"REWARD ${reward}",
            color="#000000",
            font=run,
            align="center",
        )

        file = File(fp=background.image_bytes, filename="wanted.jpg")

        #if you want to add a message then edit this or if you want to remove it then delete this line
        await ctx.send(f"Heya {member.mention}! The cops are on your tail.")

        #for sending the card
        await ctx.send(file=file)

async def setup(bot:commands.Bot):
    await bot.add_cog(Wanted(bot))