import discord
from discord.ext import commands
import requests
from config import honeyDBId
from config import honeyDBSecret
import json
import os


twitterEndpoint = "https://honeydb.io/api/twitter-threat-feed"
servicesEndpoint = "https://honeydb.io/api/services"
headers = {
            'X-HoneyDb-ApiId': honeyDBId,
            'X-HoneyDb-ApiKey': honeyDBSecret
        }
class HoneyDBCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="honeytwitter")
    async def HoneyTwitter(self, ctx):

        iocName = "IOCS.txt"

        result = requests.get(twitterEndpoint, headers=headers)
        if(result.status_code is not 200):
            await ctx.send("Error connecting to API endpoint")
            return
        try:
            j_obj = json.loads(result.content)
        except:
            await ctx.send("Hit an error loading twitter data")
            return

        with open(iocName, "w") as file:
            file.close()
        with open(iocName, 'a') as outFile:
            for obj in j_obj:
                 outFile.write(obj['remote_host'] + '\n')

            outFile.close()

        with open(iocName, "rb") as fp:
            await ctx.send("Here are the latest IOC's(IP's only) from Twitter")
            await ctx.send(file=discord.File(fp, "TwitterIOCS.txt"))
            fp.close()
        os.remove(iocName)

    @commands.command(name="honeytwittersearch")
    async def HoneyTwitterSearch(self, ctx, arg):
        result = requests.get(twitterEndpoint, headers=headers)
        if(result.status_code is not 200):
            await ctx.send("Error connecting to API endpoint")
            return
        try:
            j_obj = json.loads(result.content)
        except:
            await ctx.send("Hit an error loading twitter data")
            return

        for obj in j_obj:
            if obj['remote_host'] == arg:
                embed = discord.Embed(title="Twitter IP IOC search", color=0x00ff00)
                embed.add_field(name="Remote host", value=obj['remote_host'], inline=False)
                embed.add_field(name="Amount of mentions", value=obj['count'], inline=False)
                await ctx.channel.send(embed=embed)
    @commands.command(name="honeyservices")
    async def HoneyServices(self, ctx):
        result = requests.get(servicesEndpoint, headers=headers)
        if (result.status_code != 200):
            await ctx.send("Error connecting to API endpoint")
            return
        try:
            j_obj = json.loads(result.content)
        except:
            await ctx.send("Hit an error loading twitter data")
            return
        embed = discord.Embed(title="HoneyDB services under attack the last 24hrs", color=0x00ff00)
        for obj in j_obj:
            embed.add_field(name=obj['service'], value="Number of attacks" + " " + obj['count'], inline=False)

        await ctx.channel.send(embed=embed)





def setup(bot):
    bot.add_cog(HoneyDBCog(bot))