import discord
from discord.ext import commands
from datetime import timedelta
from discord.ext.commands import BucketType, cooldown
import random

from Others import Quotes, IMG

class motivation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Quotes'])
    @cooldown(1, 10, BucketType.user)
    async def Quote(self, ctx):
        embed = discord.Embed(
            title='Quotes',
            color=discord.Color.gold()
        )
        embed.add_field(name='Inspirational Quotes', value=f'{random.choice(Quotes.Ins)}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['VQ', 'ImgQ', 'IQuote'])
    @cooldown(1, 15, BucketType.user)
    async def ImgQuote(self, ctx):
        embed = discord.Embed(
            title='Visual Motivation',
            color=discord.Color.gold()
        )
        embed.set_image(url=f'{random.choice(Quotes.img)}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['Speeches'])
    @cooldown(1, 120, BucketType.user)
    async def Speech(self, ctx):
        embed = discord.Embed(
            title='Motivation',
            color=discord.Color.gold()
        )

        embed.add_field(name='**Speeches**', value=(
            '**Be motivated. Dont let anybody decide your future. Be strong and follow what you love.**‏‏'))
        await ctx.send(embed=embed)
        await ctx.send(file=File(f'{random.choice(IMG.speech)}'))

    @commands.command(aliases=['Gspeech', 'gs'])
    @cooldown(1, 180, BucketType.user)
    async def GreatSpeech(self, ctx):
        embed = discord.Embed(
            title='Motivation',
            color=discord.Color.gold()
        )

        embed.add_field(name='**Speeches**', value=(
            '**Your stronger than you think. Dont keep your dream in your mind. Show it. Prove the world what your made of.**‏‏'))
        await ctx.send(embed=embed)
        await ctx.send(file=File(f'{random.choice(IMG.speech)}'))

    @commands.command(aliases=['masterpiece', 'Arts', 'mp', 'Masterpieces'])
    @cooldown(1, 180, BucketType.user)
    async def Art(self, ctx):
        embed = discord.Embed(
            title='**Artworks:**',
            color=discord.Color.dark_blue()
        )
        embed.add_field(name='‏‏‎ ‎', value=f'{random.choice(art.art)}')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(motivation(bot))
