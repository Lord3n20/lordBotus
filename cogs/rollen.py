import discord
from discord.ext import commands

class guilIDchannelID(commands.Cog):
    def __init__(self, dc):
        self.dc = dc

    @commands.command()
    async def farbe(self, ctx):
        embed = discord.Embed(
            title="Farbrollen",
            color = discord.Color.green()
        )
        farbe = ctx.message.content.replace("~farbe ","")
        guild = ctx.guild
        author = ctx.message.author
        if len(farbe) != 6:
            embed.add_field(name="Nutzerfehler", value="Farben bitte im Hex-Color-Code (allerdings ohne Hashtag) angeben, sowie mit *einem* Leerzeichen zu `~farbe`. Vielen Dank.")
            await ctx.reply(embed=embed)
            return False
        if str(author.roles).find("Stammgast") == -1:
            embed.add_field(name="Nutzerfehler", value="Tut mir leid, Sie sind nicht mit der Stammgast-Rolle gesegnet")
            await ctx.reply(embed=embed)
            return False
        else:
            try:
                try:
                    print("Kaaaputtt")
                    role = discord.utils.get(author.guild.roles, name=str(author.display_name))
                    print("role")
                    await role.delete()
                    print("oke?")
                except:
                    print("nixnix")
                #if discord.utils.get(author.guild.roles, name=str(author.name)) in (author.guild.roles):
                #    return False
                botrole = discord.utils.get(guild.roles, name="Lord Botus")
                print("1")
                await guild.create_role(name=str(author.display_name), colour=discord.Colour(int(farbe, 16)))
                print("2")
                role = discord.utils.get(author.guild.roles, name=str(author.display_name))
                print("3")
                await role.edit(position=int(int(botrole.position)-2))
                print("4")
                await author.add_roles(role)
                print("5")
                embed.add_field(name="Rolle erstellt und zugewiesen", value=author.name+" hat erfolgreich seine Rolle für die Farbe #"+farbe+" erhalten")
                await ctx.reply(embed=embed)
            except Exception as e:
                embed.add_field(name="Es gab einen Fehler", value="Versuchen Sie es erneut oder kontaktieren Sie ihren Support")
                await ctx.reply(embed=embed)

def setup(dc):
    dc.add_cog(guilIDchannelID(dc))
