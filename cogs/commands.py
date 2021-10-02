from twitchio.ext import commands
import twitchio

class MyCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='slap')
    async def slap(self, ctx, person, reason='being a silly goose'):
        honked = f'{ctx.author.name} just slapped @{person} for {reason}'
        await ctx.send(honked)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def give(self, ctx: commands.Context):
        await ctx.send(f'GivePLZ GivePLZ GivePLZ GivePLZ GivePLZ GivePLZ GivePLZ GivePLZ')




def prepare(bot: commands.Bot):
    # Load cog with this module
    bot.add_cog(MyCog(bot))
