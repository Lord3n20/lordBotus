from discord.ext import commands
from discord import Embed
import os
import discord
print(discord.Intents)
bot = commands.Bot(command_prefix='~')

@bot.command()
async def reload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
    except:
        await ctx.send("Der Cog wurde noch nicht geladen und wird nun zum ersten mal geladen")
    bot.load_extension(f'cogs.{extension}')
    embed = Embed(
        title='Cogs',
        description=f'{extension} wurde erfolgreich neugeladen',
        color=0x2f9c3f
    )
    await ctx.send(embed=embed)

@bot.command()
async def start(ctx, self):
     self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Hi'))

@bot.event
async def on_command_error(ctx, error):
    try:
        embed = Embed(
            title='Halt Stop',
            description=f'Du hast einen Befehl genommen der nicht existiert!',
            color=0xff0000
        )
    except:
        embed = Embed(
            title='Glückwunsch',
            description=f'Du hast hast entweder etwas zersört oder was kaput gemacht!',
            color=0xff0000
        )
    await ctx.send(embed=embed)

try:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Der Cog {filename[:-3]} wurde erfolgreich geladen.')
except:
    for filename in os.listdir():
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Der Cog {filename[:-3]} wurde erfolgreich geladen.')






bot.run('Nzk0NTE4NTQ1OTUzMzI1MDY3.X-7_Dg.rzVRBysw-F4JAwuJDZfyUAAizhM')

