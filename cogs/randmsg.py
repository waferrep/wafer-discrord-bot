import discord
from discord.ext import commands
import random

class randmsg(commands.Cog):

    def __init__(self, client):
        self.client = client

    # I DONT NEED THIS NOW BUT KEEPING TO BE SAFE
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     rand_messages = []
    #     if "waf" in message.content.lower():
    #         if message.author == self.client.user:
    #             return
    #         async with message.channel.typing():
    #             for channelholder in message.guild.text_channels:
    #                 try:  
    #                     if channelholder.is_nsfw() or message.attachments:
    #                         pass
    #                     else:
    #                         async for messageholder in channelholder.history(limit=150):
    #                             if messageholder.system_content == "":
    #                                 continue
    #                             if messageholder.author.bot:
    #                                 continue
    #                             else:
    #                                 pass
    #                             rand_messages.append(messageholder)
    #                 except:
    #                     pass
    #         if len(rand_messages) > 0:
    #             message_to_send = random.choice(rand_messages)
    #             await message.channel.send(message_to_send.system_content)
    #     elif message.content == "":
    #         pass

async def setup(client):
    await client.add_cog(randmsg(client))