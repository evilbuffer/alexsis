import discord
from discord.ext import commands
from config import virustotalApi
import requests
import json


class VirustotalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="vtdetections")
    async def vtdetections(self, ctx, hash):
        endpoint = "https://www.virustotal.com/vtapi/v2/file/report"
        params = {'apikey': virustotalApi, 'resource': hash, 'allinfo': 'true'}
        r = requests.get(endpoint, params=params)
        j_obj = json.loads(r.content)

        if(j_obj['response_code'] == 0):
            await ctx.send("Sample is not in the Virustotal database... :(")
            return

        counter = 0
        embed = discord.Embed(title="VT detections", color=0x00ff00)
        embed2 = discord.Embed(title="VT detections", color=0x00ff00)
        for obj in j_obj['scans']:
            av = (obj)
            res = str((j_obj['scans'][obj]['result']))
            if len(res) <= 4:
                pass
            else:
                if(counter <= 24):
                    embed.add_field(name=av, value=res, inline=False)
                else:
                    embed2.add_field(name=av, value=res, inline=False)
        if(counter <= 24):
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)

    @commands.command(name="vturlcheck")
    async def vturlcheck(self, ctx, url):
        endpoint = "https://www.virustotal.com/vtapi/v2/url/report"
        params = {'apikey': virustotalApi, 'resource': url, 'allinfo': 'true'}

        embed = discord.Embed(title="VT URL check", color=0x00ff00)
        embed2 = discord.Embed(title="VT URL check",color=0x00ff00 )
        r = requests.get(endpoint, params=params)
        j_obj = json.loads(r.content)
        counter = 0
        for obj in j_obj['scans']:
            if(counter != 25):
                embed.add_field(name=obj, value=j_obj['scans'][obj]['result'], inline=False)
                counter = counter + 1
            else:
                embed2.add_field(name=obj, value=j_obj['scans'][obj]['result'], inline=False)

        if(counter <= 25):
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)


def setup(bot):
    bot.add_cog(VirustotalCog(bot))