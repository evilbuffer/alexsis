import requests
import csv
import codecs
import discord
from discord.ext import commands
from contextlib import closing
import re


class URLHausCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="25fresh")
    async def fresh25urlhaus(self, ctx):
        await ctx.send("Getting 25 fresh new malware urls, free of Gozi, Mozi and Mirai")
        miraiRegexp = re.compile(r'mirai')
        moziRegexp = re.compile(r'Mozi')
        goziRegexp = re.compile(r'Gozi')
        url = "https://urlhaus.abuse.ch/downloads/csv_online/"
        embed = discord.Embed(title="25 Newest active malware hosts")
        counter = 0
        with closing(requests.get(url, stream=True)) as r:
            reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',', quotechar='"')
            for row in reader:
                if(counter <= 9):
                    counter = counter + 1
                    pass
                elif(counter != 34):
                    domain = row[2]
                    domain = domain.replace("http://", "hxxp://")
                    domain = domain.replace("https://", "hxxps://")
                    name = row[5].replace(",", ", ")
                    if(moziRegexp.search(name)):
                        pass
                    elif(goziRegexp.search(name)):
                        pass
                    elif(miraiRegexp.search(name)):
                        pass
                    else:
                        embed.add_field(name=name, value=domain, inline=False)
                        counter = counter + 1

        await ctx.send(embed=embed)

    @commands.command(name="findmalware")
    async def findmalware(self,ctx,arg):
        query = r'{}'.format(arg)
        regexp =re.compile(query)
        url = "https://urlhaus.abuse.ch/downloads/csv_online/"
        embed = discord.Embed(title="Hits on your query", color=0xff0000)
        embed2 = discord.Embed(title="Hits on your query", color=0xff0000)
        embed3 = discord.Embed(title="Hits on your query", color=0xff0000)
        counter = 0
        with closing(requests.get(url, stream=True)) as r:
            reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',', quotechar='"')
            for row in reader:
                if (counter <= 9):
                    counter = counter + 1
                elif(counter <= 34):
                    domain = row[2]
                    domain = domain.replace("http://", "hxxp://")
                    domain = domain.replace("https://", "hxxps://")
                    name = row[5].replace(",", ", ")
                    if(regexp.search(name)):
                        embed.add_field(name=name, value=domain, inline=False)
                        counter = counter + 1
                elif(counter <= 59):
                    domain = row[2]
                    domain = domain.replace("http://", "hxxp://")
                    domain = domain.replace("https://", "hxxps://")
                    name = row[5].replace(",", ", ")
                    if (regexp.search(name)):
                        embed2.add_field(name=name, value=domain, inline=False)
                        counter = counter + 1

        finalCount = counter - 10
        if(finalCount == 50):
            msg = "Your query got {} hits [{}]".format(finalCount, "MAX AMOUNT")
        else:
            msg = "Your query got {} hits".format(finalCount)

        if(counter <= 10):
            await ctx.send("No samples found")
            return
        elif(counter <= 34):
            await ctx.send(msg)
            await ctx.send(embed=embed)
        else:
            await ctx.send(msg)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)

    @commands.command(name="findurl")
    async def findsample(self, ctx, arg):
        query = r'{}'.format(arg)
        regexp = re.compile(query)
        url = "https://urlhaus.abuse.ch/downloads/csv_online/"
        embed = discord.Embed(title="Hits on your query", color=0xff0000)
        embed2 = discord.Embed(title="Hits on your query", color=0xff0000)
        embed3 = discord.Embed(title="Hits on your query", color=0xff0000)
        counter = 0
        with closing(requests.get(url, stream=True)) as r:
            reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',', quotechar='"')
            for row in reader:
                if (counter <= 9):
                    counter = counter + 1
                elif (counter <= 34):
                    domain = row[2]
                    domain = domain.replace("http://", "hxxp://")
                    domain = domain.replace("https://", "hxxps://")
                    name = row[5].replace(",", ", ")
                    if (regexp.search(domain)):
                        embed.add_field(name=name, value=domain, inline=False)
                        counter = counter + 1
                elif (counter <= 59):
                    domain = row[2]
                    domain = domain.replace("http://", "hxxp://")
                    domain = domain.replace("https://", "hxxps://")
                    name = row[5].replace(",", ", ")
                    if (regexp.search(domain)):
                        embed2.add_field(name=name, value=domain, inline=False)
                        counter = counter + 1
        finalCount = counter - 10
        if (finalCount == 50):
            msg = "Your query got {} hits [{}]".format(finalCount, "MAX AMOUNT")
        else:
            msg = "Your query got {} hits".format(finalCount)

        if (counter <= 10):
            await ctx.send("No url found")
            return
        elif (counter <= 34):
            await ctx.send(msg)
            await ctx.send(embed=embed)
        else:
            await ctx.send(msg)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)










def setup(bot):
    bot.add_cog(URLHausCog(bot))