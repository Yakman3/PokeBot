import discord
from discord.ext import commands   
from discord import client
import pokebase as pb
import sqlite3
import random
import json
with open("pokedex.json") as f:
    filename = json.load(f)
import requests

class Memes:
    
    def __init__(self, bot):
        self.bot = bot
    '''
    @commands.command(pass_context=True)
    async def thetruepath(self,ctx):
        """SHARP TURN!"""
        em = discord.Embed(title="The only worthy exit")
        em.set_image(url="https://i.imgur.com/u5woQs4.png")
        await self.bot.say(embed = em)
    @commands.command(pass_context=True)
    async def say(self, ctx, *, something=None):
        """Coerce the bot to say whatever you want."""
        if something is None:
            await self.bot.say("What do you want to know about Pokemon?")
            await self.bot.delete_message(ctx.message)
        else:
            await self.bot.say(something)
            await self.bot.delete_message(ctx.message)
    
    @commands.group(pass_context=True)
    async def omanyte(self, ctx):
        """The helix god rises!"""
        em1 = discord.Embed(title="Hail the Helix God", description="All Hail!")
        em1.set_image(url="https://cdn.discordapp.com/attachments/399657923732570112/399659505534631945/794.png")
        await self.bot.say(embed = em1)
    @commands.command(pass_context=True)
    async def missingno(self):
        """Glitch"""
        em2 = discord.Embed(title="Missingno", description="Error. Error. Error.")
        em2.set_image(url="https://vignette.wikia.nocookie.net/vsbattles/images/d/d8/MissingNo..png/revision/latest/scale-to-width-down/480?cb=20170302202745")
        await self.bot.say(embed = em2)
    @commands.command(pass_context=True)
    async def blep(self):
        """oh h*ck"""
        emblep = discord.Embed(title="Blep", description="Heckin' Blepped")
        emblep.set_image(url="https://i.redditmedia.com/jDGZNJZLYVb7b8ZPz8opCMC3Gedq9IwPNKEV7sLrzSc.jpg?w=669&s=423abace36b880435408f1fa5e1baa9d")
        await self.bot.say(embed = emblep)
    @commands.command(pass_context=True)
    async def eatdinner(self, ctx):
        """Hungry? I got your favorite dinner."""
        emtide = discord.Embed(title="Your dinner is served, " + str(ctx.message.author) + "!", description="Bone Apple Teeth!")
        emtide.set_image(url="http://cdn.smosh.com/sites/default/files/2018/01/tide-pods-meme-hot-pockets.jpg")
        await self.bot.say(embed = emtide)
    '''
    @commands.command(pass_context=True, aliases=['nl','NL','NicLande','niclande'])
    async def nicLande(self, ctx):
        """No, his name is..."""
        Letters = ['B','C','D','F','G','H','J','K','L','M','N','P','Qu','R','S','T','V','W','X','Y','Z','Th','Ch','Sh','Br','Shm','Shl', 'Tw', 'Shn']  
        First = random.randint(0, len(Letters))
        Last = random.randint(0, len(Letters))
        F = Letters[First]
        L = Letters[Last]
        em = discord.Embed(title="Hey look, it's " + F + "ic " + L + "ande!")
        await self.bot.say(embed = em)
        
        
def setup(bot):
    bot.add_cog(Memes(bot))