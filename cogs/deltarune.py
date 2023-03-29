from posixpath import split
import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import textwrap
import re

# funcs shouldn't be within class unless related to class directly. in this case its not a command or event
def useRegex(input):
    pattern = re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", re.IGNORECASE)
    return pattern.match(input)

class deltarune(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.hybrid_command()
    async def deltarune(self, ctx, input: str = None, color: str = None, avamember : discord.Member = None): # type: ignore
        async with ctx.typing():
            if color == None or input == None or avamember == None: #condensed
                await ctx.send("Missing argument(s)!")
                return  
            # this code will never run because its checking if avamember is None, which is taken care of
            # if not avamember: 
            #     if ctx.message.attachments: #if msg has attachment use that for the image
            #         for attachment in ctx.message.attachments:
            #             await attachment.save('deltarune/userpfp2.png') 
            #         avamember = ('deltarune/userpfp2.png')
            #     # if ctx.message.match(input): fix this later, need to change avamember to string, do this if string is link, else do everything else
            #     #     await ctx.send(f'This is a test, {url}')
            #     else:
            #         avamember = ctx.author #if no avamember default to user
            if 'color' not in color and 'black' not in color: #default to black
                color = 'black'

            thefont= ImageFont.truetype('deltarune/font.ttf', 35)
            box = Image.open('deltarune/deltabox.jpg')
            input = textwrap.fill(text=input, width=25)
            if avamember != ('deltarune/userpfp2.png'):
                await avamember.avatar.save('deltarune/userpfp.png') # type: ignore
                ava = Image.open('deltarune/userpfp.png')
            else:
                ava = Image.open('deltarune/userpfp2.png')

            if color == 'black': #make black - this sucks but it works
                bwAva = ava.convert("L")
                shrink = bwAva.resize((30,30))
                pixel = shrink.resize((100, 100), Image.NEAREST)
                pixel.save("deltarune/pixelpfpbw.png")
                d1 = ImageDraw.Draw(box)
                d1.text((150, 30), "*  " + input, fill=(255, 255, 255),font=thefont)
                box.save("deltarune/boxedit.png")
                new = Image.open("deltarune/boxedit.png")
                pixel1 = Image.open('deltarune/pixelpfpbw.png')
                new.paste(pixel1, (35, 35))
                new.save('deltarune/final.png')
                await ctx.send(file=discord.File('deltarune/final.png'))

            else: #make color
                shrink = ava.resize((30,30))
                pixel = shrink.resize((100, 100), Image.NEAREST)
                pixel.save("deltarune/pixelpfp.png")
                d1 = ImageDraw.Draw(box)
                d1.text((150, 30), "*  "+ input, fill=(255, 255, 255),font=thefont)
                box.save("deltarune/boxedit.png")
                new = Image.open("deltarune/boxedit.png")
                pixel1 = Image.open('deltarune/pixelpfp.png')
                new.paste(pixel1, (35, 35))
                new.save('deltarune/final.png')
                await ctx.send(file=discord.File('deltarune/final.png'))


async def setup(client):
    await client.add_cog(deltarune(client))