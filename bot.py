from twitchio.ext import commands
from env import TOKEN
import cogs.art


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TOKEN, prefix='!', initial_channels=['Travinksy','tayyday'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')


bot = Bot()
initial_extensions = ["cogs.commands"]
for extension in initial_extensions:
    bot.load_module(extension)
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
