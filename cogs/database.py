import discord
import os
import random
from discord.ext import commands


class database(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Database ready')

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = str.lower(message.content) # semi-redundant
        if message.author.bot:
            return
        if not message.content:
            return
        if msg[0] == "-": # make sure its not a command 
            return
        if "waf" in msg:
            return
        if message.mentions:
            return
        for channel in message.guild.text_channels:
                if channel.is_nsfw():
                    pass
        data = 'realdata/' + f"{message.guild.id}" + '.txt.' # find server folder and channel file
        if os.path.exists(data): # it exists? awesome write a new line to it
            file = open(data, 'a')
            file.write(f"{message.channel.id}-{message.id}" + "\n")
            #print(f"{message.id}" + " to " + data)
            file.close
        else: #file doesn't exist? that sucks, make it
            fp = open(data, 'x')
            fp.close()
            print("created new file: " + data)

    @commands.hybrid_command()
    async def filldb(self, ctx):
        ID = 146395257313951744
        if ctx.author.id == ID:
            if ctx.author == self.client.user:
                return
            if ctx.author.bot:
                return
            async with ctx.channel.typing():
                for chnl in ctx.guild.text_channels:
                    try:
                        if chnl.is_nsfw() or not ctx.message.content:
                            pass
                        async for msgholder in chnl.history(limit=None):
                            if not msgholder.content or msgholder.content[0] == "-" or msgholder.author.bot or msgholder.mentions:
                                continue
                            data = 'realdata/' + f"{ctx.guild.id}" + '.txt.' # find server folder and channel file
                            if os.path.exists(data): # it exists? awesome write a new line to it
                                file = open(data, 'a')
                                file.write(f"{msgholder.channel.id}-{msgholder.id}" + "\n")
                                file.close
                            else: #file doesn't exist? that sucks, make it
                                fp = open(data, 'x')
                                fp.close()
                    except:
                        pass
            await ctx.channel.send(f'filled database') 
            if ctx.author.id != ID:
                await ctx.channel.send('no')
                return


    @commands.hybrid_command()
    async def cleardb(self, ctx):
        ID = 146395257313951744
        if ctx.author.id == ID:
            if ctx.author == self.client.user:
                return
            data = 'realdata/' + f"{ctx.guild.id}" + '.txt.' # find server folder and channel file
            if os.path.exists(data): # it exists? awesome write a new line to it
                file = open(data, 'w')
                file.close()
                await ctx.channel.send(f'cleared database')
        if ctx.author.id != ID:
            await ctx.channel.send('no')
            return

    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        print("channel deleted")
        with open('realdata/' + f"{channel.guild.id}.txt", "r", encoding="utf-8") as f:
            print (channel.guild.id)
            file_lines = [line.rstrip() for line in f.readlines()]
            with open(
                "realdata/" + str(channel.guild.id) + ".txt", "w", encoding="utf-8"
            ) as fw:
                for line in file_lines:
                    if str(channel.id) not in line:
                        fw.write(line + "\n")
                    else:
                        print("removed " + line)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        with open("realdata/" + str(message.guild.id) + ".txt", "r", encoding="utf-8") as f:
            file_lines = [line.rstrip() for line in f.readlines()]
            with open(
                "realdata/" + str(message.guild.id) + ".txt", "w", encoding="utf-8"
            ) as fw:
                for line in file_lines:
                    if str(message.id) not in line:
                        fw.write(line + "\n")
                    else:
                        print("removed " + line + " " + message.content)

async def setup(client):
    await client.add_cog(database(client))