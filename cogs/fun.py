import discord
from discord.ext import commands
import random
from posixpath import split
from PIL import Image, ImageDraw, ImageFont
import textwrap
import asyncio
import os
import re
from io import BytesIO


class fun(commands.Cog):
    global channels
    global funmode
    funmode = False
    channels = []

    def __init__(self, client):
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self): 
        print("Ready cog loaded") 

    #gets user info and then prints user info + msg to console
    @commands.Cog.listener()
    async def on_message(self, message):
        global funmode
        username = str(message.author).split('#')[0] 
        user_message = str(message.content)
        channel = str(message.channel.name) 
        print(f'{username}: {user_message} ({channel})') 

        if funmode == False:
            if message.author == self.client.user:
                return
        elif not message.content: 
            return
        
        randomGen1 = random.randrange(1, 6)
        #1/6 chance to repsond to one of these messages randomly
        if randomGen1 == 1:
            if "gm" in message.content.lower():
                await message.channel.send(f'GM {username}', reference=message)

            elif "gn" in message.content.lower():
                await message.channel.send(f'GN {username}', reference=message)
            
            elif "jinx" in message.content.lower()  or "cat" in message.content.lower():
                await message.channel.send('https://cdn.discordapp.com/attachments/754245502538743808/957467294156615680/9k.png')

            elif "dorchadas" in message.content.lower():
                await message.channel.send('https://media.discordapp.net/attachments/952203557724094525/957235469131874314/ezgif.com-gif-maker_2.gif')

            elif "kiby" in message.content.lower():
                await message.channel.send('https://tenor.com/view/kirby-kirby-cooked-kirby-massage-kirby-pat-massage-gif-25195626')

            elif "fish" in message.content.lower() or "fishing" in message.content.lower():
                await message.channel.send('https://cdn.discordapp.com/attachments/754245502538743808/958202794211414096/FO-32LgVUAMXEO-.png')

            elif "fire" in message.content.lower():
                react = '🔥'
                await message.add_reaction(react)

            elif "upvote" in message.content.lower():
                react = '<:upvote:957698832513237022>'
                await message.add_reaction(react)

            elif "downvote" in message.content.lower():
                print(f'{funmode}') 
                react = '<:downvote:957699003863150602>'
                await message.add_reaction(react)

        #respond to user pinging the bot
        for x in message.mentions:
            if '-' in message.content[0]:
                return
            if (x==self.client.user):
                randomGen = random.randint(1, 3) 
                if randomGen == 1:
                    await message.channel.send(f"whatttttttttttttttt", reference=message)
                elif randomGen == 2:
                    await message.channel.send(f'<@!{message.author.id}>', reference=message)
                elif randomGen == 3:
                    await message.channel.send(f'stop pinging me!!!!!', reference=message)
            
        if funmode == True:         
            if message.channel.id in channels:            
                print("WE'RE IN THE LOOP") 
                if (not message.content) or message.attachments:
                    print("NO MESSAGE CONTENT") 
                    return
                else:
                    user_message = message.clean_content
                    pattern = re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", re.IGNORECASE)
                    match = pattern.search(message.content)
                    if match:
                        processed_message = pattern.sub("", user_message)
                        user_message = processed_message
                    else:
                        avamember = message.author #if no avamember default to user
                        fontsize = 35
                        thefont = ImageFont.truetype('deltarune/font.ttf', fontsize)
                        box = Image.open('deltarune/deltabox.jpg')
                        input = textwrap.fill(text=user_message, width=25)
                        await avamember.avatar.save(f'deltarune/temp/{message.author.id}.png')
                        ava = Image.open(f'deltarune/temp/{message.author.id}.png')
                        bwAva = ava.convert("L")
                        shrink = bwAva.resize((30,30))
                        pixel = shrink.resize((100, 100), Image.NEAREST)
                        pixel.save(f'deltarune/temp/{message.author.id}bw.png')
                        d1 = ImageDraw.Draw(box)
                        d1.text((150, 30), "*  " + input, fill=(255, 255, 255),font=thefont)
                        box.save("deltarune/temp/boxedit.png")
                        new = Image.open("deltarune/temp/boxedit.png")
                        pixel1 = Image.open(f'deltarune/temp/{message.author.id}bw.png')
                        new.paste(pixel1, (35, 35))
                        new.save(f'deltarune/temp/{message.author.id}final.png')

                        await message.delete()
                        await message.channel.send(file=discord.File(f'deltarune/temp/{message.author.id}final.png'))
                        os.remove(f'deltarune/temp/{message.author.id}.png')
                        os.remove(f'deltarune/temp/{message.author.id}bw.png')
                        os.remove(f'deltarune/temp/{message.author.id}final.png')

    
    @commands.hybrid_command()
    async def rpmode(self, ctx, arg):
        global funmode
        ID = 146395257313951744
        global channels
        channels.append(ctx.channel.id)
        print(channels)
        if ctx.author.id == ID:
            async with ctx.typing():
                if arg == 'on':
                    funmode = True
                    await ctx.reply(f':3')
                    print(f'{funmode}') 
                    await ctx.channel.edit(slowmode_delay=3)
                    await asyncio.sleep(0.5) # Add a delay of 500ms
                    await ctx.send(f"Set the slowmode delay in this channel to {3} seconds!")
                elif arg == 'no':
                    funmode = False
                    await ctx.reply(f'3:')
                    print(f'{funmode}') 
                    await ctx.channel.edit(slowmode_delay=0)
                    await asyncio.sleep(0.5) # Add a delay of 500m
                    await ctx.send(f"Removed delay!")
        else:
            await ctx.reply(f'HAHA LOSER!')

                        
    @commands.hybrid_command() #random # from this range, shld add userinput to determine range someday
    async def random(self, ctx):
        async with ctx.typing():
            await ctx.reply(random.randrange(100000))

    @commands.hybrid_command() #test ping
    async def ping(self, ctx):
        async with ctx.typing():
            await ctx.reply(f'pong:  {round(self.client.latency * 1000)} ms')

    @commands.hybrid_command() #8ball command
    async def yesno(self, ctx):
        async with ctx.typing():
            randomGen = random.randint(1, 6) 
            if randomGen == 1:
                await ctx.reply(f'no')
            elif randomGen == 2:
                await ctx.reply(f'yes')
            elif randomGen == 3:
                await ctx.reply(f'maybe')
            elif randomGen == 4:
                await ctx.reply(f'try again')
            elif randomGen == 5:
                await ctx.reply(f'absolutely')
            elif randomGen == 6:
                await ctx.reply(f'negative')

    @commands.hybrid_command() #sends a users avatar
    async def ava(self, ctx, avamember : discord.Member=None):
        if avamember == None:
            await ctx.send("Missing argument(s)!")
            return
        async with ctx.typing():
            userAvatarUrl = avamember.avatar
            await ctx.send(userAvatarUrl)


async def setup(client):
    await client.add_cog(fun(client))
