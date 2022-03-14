import discord
from discord.ext import commands
import time

def reverse(s):
   a=""
   last_index=len(s)-1
   for i in range(last_index,-1,-1):
      a=a+s[i]
   return a

class add(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def r(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(ctx.message.author.name + ": " + reverse(ctx.message.content.replace("~r ", '')))

def setup(dc):
    dc.add_cog(add(dc))
