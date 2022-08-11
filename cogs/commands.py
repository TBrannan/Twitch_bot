from secrets import choice
from twitchio.ext import commands
import cogs.art as art
from random import choice
import requests

class MyCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='slap')
    async def slap(self, ctx, person, *args, reason='being a silly goose'):
        if len(args) > 0:
            x = ' '.join(args)
            honked = f'{ctx.author.name} just slapped {person} for {x}'
            await ctx.send(honked)
        else:
            honked = f'{ctx.author.name} just slapped {person} for {reason}'
            await ctx.send(honked)

    @commands.command(name='ban')
    async def ban(self, ctx, person, *args, reason='permanently banned'):
        if len(args) > 0:
            x = ' '.join(args)
            honked = f'{person} was just permanently banned for {x}'
            await ctx.send(honked)
        else:
            honked = f'{person} was just permanently banned for {choice(art.randy)}'
            await ctx.send(honked)

    @commands.command(name="poke")
    async def poke(self, ctx):
        # -*- coding: utf-8 -*-
        import random as r
        f = [i for i in range(895) if i !=0]
        x = r.choice(f)
        url = f'https://pokeapi.co/api/v2/pokemon/{x}'
        response = requests.get(url)
        poke = response.json()
        name = poke["name"]
        icon = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{x}.png'
        link = f'https://www.google.com/search?tbm=isch&as_q=rule+34+{name}+pokemon'
        await ctx.send(f"{name}\n{icon}")

    @commands.command(name='death+')
    async def death(self, ctx):
            await ctx.send(art.died)

    @commands.command(name='crourb')
    async def crourb(self, ctx):
            await ctx.send(art.crourb)

    @commands.command(name='catjam')
    async def catjam(self, ctx):
        await ctx.send(art.catjam)

    @commands.command(name='bbpepe')
    async def bbpepe(self, ctx):
        await ctx.send(art.bbpepe)

    @commands.command(name='booba')
    async def booba(self, ctx):
        await ctx.send(art.booba)

    @commands.command(name='hank')
    async def hank(self, ctx):
        await ctx.send(art.hank)

    @commands.command(name='activate')
    async def activate(self, ctx):
        await ctx.send(art.activate)

    @commands.command(name='fish')
    async def fish(self, ctx):
        await ctx.send(art.fish)

    @commands.command(name='duck')
    async def duck(self, ctx):
        await ctx.send(art.duck)

    @commands.command(name='mboob')
    async def mboob(self, ctx):
        await ctx.send(art.mboob)

    @commands.command(name='goose')
    async def goose(self, ctx):
        await ctx.send(art.goose)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def give(self, ctx: commands.Context):
        await ctx.send(f'GivePLZ GivePLZ GivePLZ GivePLZ GivePLZ GivePLZ GivePLZ GivePLZ')


def prepare(bot: commands.Bot):
    # Load cog with this module
    bot.add_cog(MyCog(bot))
