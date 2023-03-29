import discord
import os
import asyncio
from discord.ext import commands
from discord.ext import tasks


TOKEN = 'OTU3MzkzMTg1NjExNTk5OTIz.GqqeEO.KyE9yOod4l0SZnEINq_QL7rHKFcgPdiOxZaVRg'
ID = 146395257313951744

async def main():
    #start client
    async with client:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await client.load_extension(f'cogs.{filename[:-3]}') 
        await client.start(TOKEN)


intents = discord.Intents().all()
client = commands.Bot(command_prefix="-", intents=intents)

@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(f"Sycned {len(synced)} commands!")
    except Exception as e:
        print(e)
    print('I am ready')

@client.command()
async def load(ctx, extension):
    if ctx.author.id == ID:
        await client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} loaded.')
    if ctx.author.id != ID:
        await ctx.send('no')


@client.command()
async def unload(ctx, extension, avamember : discord.Member=None):
    if ctx.author.id == ID:
        await client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} unloaded.')
    if ctx.author.id != ID:
        await ctx.send('no')

discord.utils.setup_logging()
asyncio.run(main())