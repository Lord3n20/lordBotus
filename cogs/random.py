import discord
from discord.ext import commands
import time
import random

class add(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def random(self, ctx):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(' mit Menschen die ~help tippen'))
        await ctx.send(random.randint(0,100))
def setup(dc):
    dc.add_cog(add(dc))
