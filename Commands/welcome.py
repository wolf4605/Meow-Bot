import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, Font, load_image
import random
from num2words import num2words

class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Just a Event to ensure the cog is loading
    @commands.Cog.listener()
    async def on_ready(self):
        print("______________")
    
    async def cog_load(self):
        print (f"{self.__class__.__name__} command has been loaded.")

    #The Command
    @commands.hybrid_command()
    async def welcome(self, ctx: commands.context, member: discord.Member):

        """Create a welcome card"""

        pos = sum(m.joined_at < member.joined_at for m in member.guild.members
        if m.joined_at is not None)

        pos_in_words = num2words(pos, to='ordinal')

        # list of possible background images
        backgrounds = ["wlcbg.jpg", "wlcbg2.jpg", "wlcbg3.jpg"]

            # randomly select a background image
        random.shuffle(backgrounds)

        for selected_background in backgrounds:

            background = Editor(selected_background)

            # Card 1
            if selected_background == "wlcbg.jpg":
                background = Editor("wlcbg.jpg")
                profile_image = load_image(str(member.display_avatar.url))

                profile = Editor(profile_image).resize((400, 400)).circle_image()
                strange = Font("Strange.ttf", size=120)
                Pills = Font("NightmarePills.ttf", size=70)
                story = Font("NightmareStory.ttf", size=150)

                background.paste(profile, (1025, 100))
                background.ellipse(
                    (1025, 100),
                    400,
                    400,
                    outline="#ffffff",
                    stroke_width=8,
                )

                background.text(
                    (1250, 550),
                    "WELCOME TO THE TOWN OF DEAD",
                    color="#ffffff",
                    font=strange,
                    align="center",
                )

                background.text(
                    (1250, 675),
                    f"{member.guild.name}",
                    color="#880808",
                    font=story,
                    align="center",
                )

                background.text(
                    (1250, 875),
                    f"You are the {pos_in_words} Wandering Soul",
                    color="#ffffff",
                    font=Pills,
                    align="center",
                )

                background.text(
                    (1250, 950),
                    "Beware: You are being watched",
                    color="#ffffff",
                    font=Pills,
                    align="center",
                )

    
                #Use elif when adding more pitures
            elif selected_background == "wlcbg3.jpg":
                background = Editor("wlcbg3.jpg")
                profile_image = load_image(str(member.display_avatar.url))

                profile = Editor(profile_image).resize((500, 500)).circle_image()
                strange = Font("Strange.ttf", size=120)
                Pills = Font("NightmarePills.ttf", size=70)
                story = Font("NightmareStory.ttf", size=150)

                background.paste(profile, (425, 100))
                background.ellipse(
                    (425, 100),
                    500,
                    500,
                    outline="#ffffff",
                    stroke_width=8,
                )

                background.text(
                    (650, 650),
                    "WELCOME TO THE TOWN OF DEAD",
                    color="#ffffff",
                    font=strange,
                    align="center",
                )

                background.text(
                    (650, 775),
                    f"{member.guild.name}",
                    color="#880808",
                    font=story,
                    align="center",
                )

                background.text(
                    (650, 975),
                    f"You are the {pos_in_words} Wandering Soul",
                    color="#ffffff",
                    font=Pills,
                    align="center",
                )

                background.text(
                    (650, 1050),
                    "Beware: You are being watched",
                    color="#ffffff",
                    font=Pills,
                    align="center",
                )
            else: 
                background = Editor("wlcbg2.jpg")
                profile_image = load_image(str(member.display_avatar.url))

                profile = Editor(profile_image).resize((250, 250)).circle_image()
                strange = Font("Strange.ttf", size=70)
                Pills = Font("NightmarePills.ttf", size=40)
                story = Font("NightmareStory.ttf", size=80)

                background.paste(profile, (230, 65))
                background.ellipse(
                    (230, 65),
                    250,
                    250,
                    outline="#ffffff",
                    stroke_width=8,
                )

                background.text(
                    (385, 350),
                    "WELCOME TO THE TOWN OF DEAD",
                    color="#ffffff",
                    font=strange,
                    align="center",
                )

                background.text(
                    (385, 430),
                    f"{member.guild.name}",
                    color="#880808",
                    font=story,
                    align="center",
                )

                background.text(
                    (385, 530),
                    f"You are the {pos_in_words} Wandering Soul",
                    color="#ffffff",
                    font=Pills,
                    align="center",
                )

                background.text(
                    (385, 580),
                    "Beware: You are being watched",
                    color="#ffffff",
                    font=Pills,
                    align="center",
                )

        file = File(fp=background.image_bytes, filename="wlcbg.jpg")

        #if you want to message more message then you can add like this
        embed = discord.Embed(
        title=f"Welcome {member.display_name}!",
        description=f"Heya {member.mention}! Welcome to {member.guild.name}. We are glad to have you here with us. You can give us a brief introduction of yourself if you play Toram Online in <#1101787219267690646>.\nEnjoy your stay.\nOh and\n!!!Happy Killing!!!",
        color=0xffffff
        )
        await ctx.send(embed=embed)
        await ctx.send(file=file)

async def setup(bot: commands.Bot):
    await bot.add_cog(Welcome(bot))