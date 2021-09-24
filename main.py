import discord
from discord.ext import commands
from discord.utils import get
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)

description = '''Oficjalny bot StylowaMC.PL'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>>', description=description, intents=intents)

@bot.event #events
async def on_ready():
  print('Zalogowalismy sie jako {0.user.name}'.format(bot))

@bot.command()
@commands.has_permissions(manage_roles=True)
async def ogloszenie(ctx, channel:discord.TextChannel,title:str, *, message: str):

    bot.get_channel(channel.id)
    emoji = discord.utils.get(bot.emojis, name='logo')
    embedVar = discord.Embed(title = str(emoji)+" StylowaMC "+str(emoji),color=0x00ff00)
    embedVar.add_field(name=title,value=message,inline=False)
    await channel.send(embed=embedVar)

bot.run('tokenhere')
