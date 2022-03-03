import discord
from discord.ext import commands
from discord.utils import get
import pandas as pd
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


@bot.event  # events
async def on_ready():
    print('Zalogowalismy sie jako {0.user.name}'.format(bot))


@bot.command()
@commands.has_permissions(manage_roles=True)
async def ogloszenie(ctx, channel: discord.TextChannel, title: str, *, message: str):
    bot.get_channel(channel.id)
    emoji = discord.utils.get(bot.emojis, name='logo')
    embedVar = discord.Embed(title=str(emoji) + " StylowaMC " + str(emoji), color=0x00ff00)
    embedVar.add_field(name=title, value=message, inline=False)
    await channel.send(embed=embedVar)


@bot.command()
async def parkour(ctx):
    emoji = discord.utils.get(bot.emojis, name='logo')
    embedVar = discord.Embed(title=str(emoji) + " StylowaMC " + str(emoji), color=0x00ff00)
    df = pd.read_csv('ranking2.csv', sep=';', index_col=False)
    df_names = df ['Nick'].to_list()
    df_scores = df ['Wynik'].to_list()
    df_time = df ['Panowanie'].to_list()
    df_days = df ['Dni'].to_list()
    result = ''
    counter = 0
    for x in df_scores:
        result += " **"+str((counter+1))+"** " + str(df_names [counter]) + " **Wynik:**" + str(df_scores [counter]) + " **Czas panowania:**" + str(
            df_days [counter]) + "dni" + " **Dzien:**" + str(df_time [counter]) + "\n"
        counter += 1
    result+="**Ostatnia aktualizacja 03.03.2022**"
    embedVar.add_field(name="Lobby Parkour Rekordy:", value=result, inline=False)
    await ctx.send(embed=embedVar)

@bot.command()
async def top3(ctx):
    emoji = discord.utils.get(bot.emojis, name='logo')
    embedVar = discord.Embed(title=str(emoji) + " StylowaMC " + str(emoji), color=0x00ff00)
    df = pd.read_csv('top3.csv', sep=';', index_col=False)
    df_names = df ['nick'].to_list()
    df_scores = df ['wynik'].to_list()
    df_time = df ['data'].to_list()
    result = ''
    counter = 0
    for x in df_scores:
        result += " **"+str((counter+1))+"** " + str(df_names [counter]) + " **Wynik:**" + str(df_scores [counter])+ " **Dzien:**" + str(df_time [counter]) + "\n"
        counter += 1
    result+="**Ostatnia aktualizacja 03.03.2022**"
    embedVar.add_field(name="Lobby Parkour TOP3:", value=result, inline=False)
    await ctx.send(embed=embedVar)


bot.run('token here')
