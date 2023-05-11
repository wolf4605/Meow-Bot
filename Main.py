#imported modules
import discord
from discord.ext import commands
from discord.ext.commands import Bot, DefaultHelpCommand
from discord import File
from easy_pil import Editor, Font, load_image
from num2words import num2words
import random
import os
from discord.ext.commands import Bot, DefaultHelpCommand
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.all() # Setting up intents I was lazy so enabled all intents

prefixes = ['amy ', 'Amy ', 'amy', 'Amy'] # The Prefix for your Bot
prefix_all=[prefix + ' ' for prefix in prefixes]
# Customizing The Default Help Command
class CustomHelpCommand(DefaultHelpCommand):
    def get_ending_note(self):
        return None

    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(
                                description=page.replace('`', ''),
                                color=random.randint(0, 0xFFFFFF))
            embed.set_author(icon_url=(self.context.bot.user.display_avatar),
                                name="__List of Commands__")
            embed.set_footer(text=f"For more info on a command use\n{self.context.prefix} help <command>.")
            await destination.send(embed=embed)

    def add_indented_commands(self, commands, heading, max_size=None):
        if not commands:
            return
        for command in commands:
            self.paginator.add_line(f'{self.context.prefix}{command.name} -- {command.short_doc}')

def main():
    bot = commands.Bot(command_prefix=prefixes, intents=intents, help_command=CustomHelpCommand())

    @bot.event
    #Welcome Message when a user joins the server
    async def on_member_join(member):

        #add the channel id in which you want to send the card
        channel = bot.get_channel(1101317581979258880) #Besure to change this

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
        await channel.send(embed=embed)
        await channel.send(file=file)
    @bot.event
    # To Ensure that the Bot logged in
    async def on_ready():
        print(f"{bot.user} Has Successfully Logged In")
    #Loading the cogs
        for filename in os.listdir("Commands"):
            if filename.endswith(".py"):
                await bot.load_extension(f"Commands.{filename[:-3]}")


    #sync app_commands
        await bot.tree.sync()
        print(f"Synced commands for {bot.user}")
        
    bot.run(TOKEN)

if __name__ == '__main__':
    main()