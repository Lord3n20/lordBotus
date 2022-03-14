import discord
from discord.ext import commands
import time

bergneustadt = "https://www.stadt-bergneustadt.de/fileadmin/webcam/image.jpg"
wiehl = "https://www.wiehl.de/webcam/image.jpg"
hueckeswagen = "http://schloss-stadt-hueckeswagen.de/Webcam/webcam.jpg"
lindlar = "http://lindlarcam.no-ip.info/record/current.jpg"
gummersbach = "https://archiv.oberberg-aktuell.de/images/webcam/image.jpg"
radevormwald = "https://images.webcamgalore.com/webcamimages/webcam-001518.jpg"
wipperfuerth = "https://www.wipperfuerth.de/fileadmin/webcam/image000.jpg"
unbekannt = "https://cdn.discordapp.com/attachments/894298127497048064/894869602897633290/unknown.png"
dresden = "https://static.dw.com/image/45974885_401.jpg"

class webCam(commands.Cog):
    def __init__(self, dc):
        self.dc = dc

    @commands.command()
    async def webcam(self, ctx):
        link = "kein link"
        stadt = ctx.message.content.replace("~webcam ", "")
        if stadt in {"Bergneustadt", "bergneustadt"}:
            link = bergneustadt
        elif stadt in {"Wiehl", "wiehl"}:
            link = wiehl
        elif stadt in {"Hückeswagen", "Hueckeswagen", "hueckeswagen", "hückeswagen"}:
            link = hueckeswagen
        elif stadt in {"Lindlar", "lindlar"}:
            link = lindlar
        elif stadt in  {"Gummersbach", "gummersbach"}:
            link = gummersbach
        elif stadt in {"Radevormwald", "radevormwald"}:
            link = radevormwald
        elif stadt in {"Wipperfürth", "wipperfuehrt", "Wipperfuehrt", "wipperführt"}:
            link = wipperfuerth
        elif stadt == {"Dresden", "dresden"}:
            link = dresden
        elif stadt == "EasterEgg":
            link = "https://www.youtube.com/watch?v=aboZctrHfK8"

        link = link+'?bild='+str(time.time())

        if stadt in {"help", "hilfe", "Help", "Hilfe"}:
            embed = discord.Embed(
                title="Hilfe für die OBK-Webcam",
                color = discord.Color.orange(),
            )
            embed.add_field(value='Siehe Bild', name="Gemeinden")
            embed.set_image(url = "https://github.com/MikeMottonix/Ms-Teams-Stuff/raw/main/Screenshot%202021-04-12%20214516.png")
            await ctx.send(embed=embed)
        else:
            if link.startswith("kein link"):
                link = unbekannt
                link = link+'?bild='+str(time.time())
            embed = discord.Embed(
                title="Webcam von " + stadt,
                color = discord.Color.blue(),
            )
            embed.set_image(url = link)
            await ctx.send(embed=embed)
def setup(dc):
    dc.add_cog(webCam(dc))
