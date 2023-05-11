import discord
from discord.ext import commands
import requests
import random
import asyncio

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

class Anime_Recommendation(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.genre_list = []

        # Fetch the list of genres from the AniList API
        url = 'https://graphql.anilist.co'
        query = '''
        query {
            GenreCollection
        }
        '''
        response = requests.post(url, json={'query': query}).json()
        self.genre_list = response['data']['GenreCollection']

        # Filter out any invalid genres
        self.genre_list = [genre.lower() for genre in self.genre_list if genre.lower()]

    @commands.command()
    async def recommend(self, ctx, *genres:str):
    # Convert genres to lowercase and remove any duplicates
        genres = list(set(genre.lower() for genre in genres))

        # Check if all genres are valid
        invalid_genres = set(genres) - set(self.genre_list)
        if invalid_genres:
            await ctx.send(f"The following genres are not valid: {', '.join(invalid_genres)}.")
            return

        # Construct the GraphQL query for fetching anime recommendations
        url = 'https://graphql.anilist.co'
        query = f'''
        query ($genres: [String]) {{
            Page {{
                media (type: ANIME, genre_in: $genres, sort: SCORE_DESC) {{
                    id
                    title {{
                        romaji
                        english
                    }}
                    coverImage {{
                        large
                    }}
                }}
            }}
        }}
        '''
        variables = {
            'genres': genres
        }
        response = requests.post(url, json={'query': query, 'variables': variables}).json()
        if response is not None:
            anime_list = response['data']['Page']['media']

        if not anime_list:
            await ctx.send(embed=discord.Embed(title="No Match Found",description="It seems that there are no anime found with your requirements", color=random.randint(0, 0xFFFFFF)))
            return

        # Limit the list of recommended anime to 5
        anime_list = anime_list[:5]

        # Create an embed message with the recommended anime
        embed = discord.Embed(title=f"Recommendation for '{', '.join(genres)}' Genres", color=random.randint(0, 0xFFFFFF))
        for i, anime_data in enumerate(anime_list):
            title = anime_data['title']['english'] or anime_data['title']['romaji']
            embed.add_field(name=f"{i+1}. {title}", value=f"**Genres:** {anime_data['id']}\n", inline=False)
        embed.set_footer(text="Type the number of the anime you want more information on.")

        message = await ctx.send(embed=embed)

        # Wait for user's reply with the number of the anime they want more information on
        def reply_check(message):
            return message.author == ctx.author and message.content.isdigit() and int(message.content) <= len(anime_list)

        reply_message = await self.bot.wait_for('message', check=reply_check, timeout=30)
        anime_data = anime_list[int(reply_message.content)-1]

        anime_info = search_anime(title)

        embed = discord.Embed(title=f"__Romaji Name:__ {anime_data['title']['romaji']}\n\n__English Name:__ {anime_data['title']['english']}", color=random.randint(0, 0xFFFFFF), description=f"Summary:\n{anime_info['description']}")
        embed.add_field(name="Format", value=anime_info['format'], inline=True)
        embed.add_field(name="Episodes", value=anime_info['episodes'], inline=True)
        embed.add_field(name="Status", value=anime_info['status'], inline=True)
        embed.add_field(name="Duration", value=anime_info['duration'], inline=True)
        embed.add_field(name="Genres", value=", ".join(anime_info['genres']), inline=True)
        embed.add_field(name="Other Names", value=anime_info['synonyms'], inline=True)
        embed.set_thumbnail(url=anime_info['coverImage']['large'])
        embed.set_image(url=anime_info['bannerImage'])
        embed.set_footer(text="React with ✅ below to get this message in your dm for bookmarking")
        await reply_message.delete()
        await message.edit(embed=embed)
        await message.add_reaction('✅')
        def dm_check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        
        try:
            await self.bot.wait_for('reaction_add', check=dm_check, timeout=10)
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
    await bot.add_cog(Anime_Recommendation(bot))
