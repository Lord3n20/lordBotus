import discord
from discord.ext import commands

class guilIDchannelID(commands.Cog):
    def __init__(self, dc):
        self.dc = dc

    @commands.command()
    async def ids(self, ctx):
        embed = discord.Embed(
            title="IDs fuer diese Nachricht",
            color = discord.Color.green()
        )
        embed.add_field(name="Server ID", value=ctx.guild.id)
        embed.add_field(name="Channel ID", value=ctx.channel.id)
        embed.add_field(name="Deine ID", value=ctx.author.id)
        embed.add_field(name="Nachrichten ID", value=ctx.message.id)
        await ctx.reply(embed=embed)

def setup(dc):
    dc.add_cog(guilIDchannelID(dc))
