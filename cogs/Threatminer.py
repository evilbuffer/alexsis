import discord
from discord.ext import commands
import requests
import json



class Threatminercog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="tmdetection")
    async def tmdetection(self, ctx, arg):
        endpoint = "https://api.threatminer.org/v2/sample.php?q={}&rt=6".format(arg)
        r = requests.get(endpoint)
        try:
            j_obj = json.loads(r.content)
        except:
            await ctx.send("Error loading json..... :(")
            return

        if(j_obj['status_code'] == '404'):
            await ctx.send("No detections for this sample...")
            return
        embed = discord.Embed(title="Threatminer AV detections", color=0x00ff00)
        for detection in j_obj['results']:
            for d in detection['av_detections']:
                embed.add_field(name=d['av'] or "null", value=d['detection'] or "null", inline=False)

        await ctx.send(embed=embed)

    @commands.command(name="hosts")
    async def hosts(self, ctx, arg):
        endpoint = "https://api.threatminer.org/v2/sample.php?q={}&rt=3".format(arg)
        r = requests.get(endpoint)
        try:
            j_obj = json.loads(r.content)
        except:
            await ctx.send("Error loading json... :(")
            return

        if(j_obj['status_code'] == '404'):
            await ctx.send("Sample not known...")
            return
        embed = discord.Embed(title="Extracted domains/ips")
        for host in j_obj['results']:
            for h in host['domains']:
                embed.add_field(name=h['domain'] or "null", value=h['ip'] or "null", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="tmfileinfo")
    async def threatminer_fileinfo(self, ctx, arg):
        endpoint = "https://api.threatminer.org/v2/sample.php?q={}&rt=1".format(arg)
        r = requests.get(endpoint)
        try:
            j_obj = json.loads(r.content)
        except:
            await ctx.send("Error loading json... :(")
            return

        if(j_obj['status_code'] == '404'):
            await ctx.send("Sample not known...")
            return
        else:

            embed = discord.Embed(title="File info")

            for result in j_obj['results']:
                embed.add_field(name="File name", value=result['file_name'] or "null", inline=False)
                embed.add_field(name="File type", value=result['file_type'] or "null", inline=False)
                embed.add_field(name="File size", value=result['file_size'] or "null", inline=False)
                embed.add_field(name="IMP hash", value=result['imphash'] or "null", inline=False)
            await ctx.send(embed=embed)

    @commands.command(name="APT")
    async def APT(self, ctx, arg):
        endpoint = "https://api.threatminer.org/v2/reports.php?q={}&rt=1".format(arg)
        r = requests.get(endpoint)
        try:
            j_obj = json.loads(r.content)
        except:
            await ctx.send("Error loading JSON... :(")
            return

        if(j_obj['status_code'] == '404'):
            await ctx.send("Didn't find any notes...")
            return
        embed = discord.Embed(title="APT notes")
        embed2 = discord.Embed(title="APT notes")
        counter = 0
        for result in j_obj['results']:
            if(counter != 24):
                embed.add_field(name=result['filename'] or "null", value=result['URL'] or "null", inline=False)
                counter = counter + 1
            else:
                embed2.add_field(name=result['filename'] or "null", value=result['URL'] or "null", inline=False)
        if(counter <= 24):
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)




def setup(bot):
    bot.add_cog(Threatminercog(bot))
