import discord
from discord.ext import commands
import time

class add(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('~help'))
        await ctx.send("Wir werden uns sehr bald um deine Webcam kümmern")
        
        channel = self.client.get_channel(840157619083018240)

        await channel.send(ctx.message.content.replace("~add", str(ctx.message.author.name) + " würde gerne folgende Webcam haben:"))
def setup(dc):
    dc.add_cog(add(dc))
