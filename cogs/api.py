from logging import exception
import discord
from discord.ext import commands
import aiohttp
import textwrap
import urllib
import asyncio
import datetime
import random
from pexels_api import API
import requests
import config
class api(commands.Cog):

    def __init__(self, client):
        self.client = client

    try:
        from googlesearch import search 
    except ImportError:
        print("No module found!")

    @commands.Cog.listener()
    async def on_ready(self):
        print("ready")

    @commands.hybrid_command()
    async def imgsearch(self, ctx, *, query):
        async with aiohttp.ClientSession() as session:
            try:
                api = API(config.API_KEY)
                api.search(query,results_per_page=100)
                photos = api.get_entries()
                print("Total results: ", api.total_results)
                if photos:
                    random_photo = random.choice(photos)
                    await ctx.send(content=str(random_photo.original))
            except Exception as e:
                await ctx.send(f"An error occurred: {str(e)}")


    @commands.hybrid_command()
    async def redpanda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/endpoints/animal/red_panda')
            pogjson = await request.json()
        fact = pogjson['fact']
        embed = discord.Embed(color=discord.Color.red(), description=fact)
        embed.set_image(url=pogjson['image'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/panda')
            pogjson = await request.json()
        fact = pogjson['fact']
        embed = discord.Embed(color=discord.Color.default(), description=fact)
        embed.set_image(url=pogjson['image'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/dog')
            dogjson = await request.json()
        fact = dogjson['fact']
        embed = discord.Embed(color=discord.Color.green(), description=fact)
        embed.set_image(url=dogjson['image'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def birb(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/bird')
            birdjson = await request.json()
        fact = birdjson['fact']
        embed = discord.Embed(color=discord.Color.blue(), description=fact)
        embed.set_image(url=birdjson['image'])
        await ctx.send(embed=embed)    

    @commands.hybrid_command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/cat')
            catjson = await request.json()
        fact = catjson['fact']
        embed = discord.Embed(color=discord.Color.teal(), description=fact)
        embed.set_image(url=catjson['image'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def raccoon(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/raccoon')
            racjson = await request.json()
        fact = racjson['fact']
        embed = discord.Embed(color=discord.Color.lighter_grey(), description=fact)
        embed.set_image(url=racjson['image'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/fox')
            foxjson = await request.json()
        fact = foxjson['fact']
        embed = discord.Embed(color=discord.Color.orange(), description=fact)
        embed.set_image(url=foxjson['image'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def koala(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/koala')
            koalajson = await request.json()
        fact = koalajson['fact']
        embed = discord.Embed(color=discord.Color.dark_gray(), description=fact)
        embed.set_image(url=koalajson['image'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def animequote(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/quote')
            animejson = await request.json()
        sentence = animejson['sentence']
        char = animejson['character']
        anime = animejson['anime']
        embed = discord.Embed(color=discord.Color.teal(), description="**" + sentence + "**\n\n " + char + "\n\n" + anime)
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def animehug(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/hug')
            animejson = await request.json()
        embed = discord.Embed(color=discord.Color.magenta())
        embed.set_image(url=animejson['link'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def animewink(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/wink')
            animejson = await request.json()
        embed = discord.Embed(color=discord.Color.magenta())
        embed.set_image(url=animejson['link'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def animebruh(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/face-palm')
            animejson = await request.json()
        embed = discord.Embed(color=discord.Color.magenta())
        embed.set_image(url=animejson['link'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def animepat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/pat')
            animejson = await request.json()
        embed = discord.Embed(color=discord.Color.magenta())
        embed.set_image(url=animejson['link'])
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/others/joke')
            jokejson = await request.json()
        joke = jokejson['joke']
        embed = discord.Embed(color=discord.Color.random(), description=joke)
        await ctx.send(embed=embed)
    
async def setup(client):
    await client.add_cog(api(client))

    