import discord
from discord.ext import commands
import requests
import asyncio
import random

def search_anime(anime_name):
    url = 'https://graphql.anilist.co'
    query = '''
    query ($search: String) {
    Media (search: $search, type: ANIME) {
        title {
        romaji
        english
        }
        description
        episodes
        format
        status
        synonyms
        duration
        genres
        bannerImage
        coverImage {
        large
        }
        trailer {
        id
        site
        }
        siteUrl
    }
    }
    '''
    variables = {
        'search': anime_name
    }
    response = requests.post(url, json={'query': query, 'variables': variables}).json()
    anime_data = response['data']['Media']
    return anime_data

class Anime_Search(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot



    @commands.hybrid_command()
    async def anime(self, ctx,*,anime_name):
        url = 'https://graphql.anilist.co'
        query = '''
        query ($search: String) {
        Page {
            media (search: $search, type: ANIME) {
            id
            title {
                romaji
                english
            }
            synonyms
            coverImage {
                large
            }
            }
        }
        }
        '''
        variables = {
            'search': anime_name
        }
        response = requests.post(url, json={'query': query, 'variables': variables}).json()
        anime_list = response['data']['Page']['media']

        if not anime_list:
            await ctx.send(f"No anime found for '{anime_name}'.")
            return

        embed = discord.Embed(title="Anime Search Results", color=random.randint(0, 0xFFFFFF))
        for i, anime_data in enumerate(anime_list):
            title = anime_data['title']['english'] or anime_data['title']['romaji']
            embed.add_field(name=f"{i+1}. {title}", value=f"ID: {anime_data['id']}\n", inline=False)
            if i == 9:
                break

        embed.set_footer(text=f"Enter a number from 1 to {min(len(anime_list), 10)} to get more information.")
        message = await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            user_input = await self.bot.wait_for('message', check=check, timeout=30)
            selected_index = int(user_input.content) - 1
            if selected_index < 0 or selected_index >= len(anime_list):
                await ctx.send("Invalid selection.")
                return
        except asyncio.TimeoutError:
            await ctx.send("Timeout. Please try again.")
            return
        except ValueError:
            await ctx.send("Invalid selection.")
            return

        anime_data = search_anime(anime_list[selected_index]['title']['romaji'])
        embed = discord.Embed(title=f"__Romaji Name:__ {anime_data['title']['romaji']}\n\n__English Name:__ {anime_data['title']['english']}", description=f"Summary:\n{anime_data['description']}", color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=anime_data['bannerImage'])
        embed.set_thumbnail(url=anime_data['coverImage']['large'])
        embed.add_field(name='Format', value=anime_data['format'])
        embed.add_field(name='Episodes', value=anime_data['episodes'])
        embed.add_field(name='Duration', value=anime_data['duration'])
        embed.add_field(name='Genres', value=', '.join(anime_data['genres']))
        embed.add_field(name='Other Names', value=anime_data['synonyms'])
        embed.add_field(name='Status', value=anime_data['status'])
        embed.set_footer(text="React with ✅ below to get this message in your dm for bookmarking")
        await user_input.delete()
        await message.edit(embed=embed)
        await message.add_reaction('✅') 

        def dm_check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
            
        try:
            reaction, user = await self.bot.wait_for('reaction_add', check=dm_check, timeout=10)
            await ctx.author.send(embed=embed)
        except asyncio.TimeoutError:
            pass

    #Just a Event to ensure the cog is loading
    @commands.Cog.listener()
    async def on_ready(self):
        print("______________")
    
    async def cog_load(self):
        print (f"{self.__class__.__name__} command has been loaded.")

async def setup(bot:commands.Bot):
    await bot.add_cog(Anime_Search(bot))