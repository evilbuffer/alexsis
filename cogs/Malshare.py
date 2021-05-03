import discord
from discord.ext import commands
from config import malshareApi
import requests
import json
import os
import subprocess
from config import pathTo7z
from config import pathToVXCage

class MalshareCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="25md5")
    async def malshare_25newmd5(self, ctx):
        endpoint = "https://malshare.com/api.php/?api_key={}&action=getlist".format(malshareApi)
        r = requests.get(endpoint)
        endpoint_json = json.loads(r.text)
        msg = []
        counter = 0
        embed = discord.Embed(title="25 MD5 hashes from Malshare, the last 24hrs", color=0x00ff00)

        for j_obj in endpoint_json:
            if(counter != 24):
                counter = counter + 1
                embed.add_field(name="MD5", value=j_obj['md5'])


        await ctx.channel.send(embed=embed)
    @commands.command(name="gettypes")
    async def malshare_gettypes(self, ctx):
        endpoint = "https://malshare.com/api.php/?api_key={}&action=gettypes".format(malshareApi)
        embed = discord.Embed(title="Malshare file types, in the last 24hrs", color=0x00ff00)

        r = requests.get(endpoint)
        j_obj = json.loads(r.text)
        
        for obj in j_obj:
            embed.add_field(name=obj, value=j_obj[obj], inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command(name="getmalware")
    async def malshare_downloadfile_by_hash(self, ctx, arg):
        endpoint = "https://malshare.com/api.php/?api_key={}&action=getfile&hash={}".format(malshareApi, arg)
        r = requests.get(endpoint)
        if(r.status_code == 500):
            await ctx.send("Invalid hash")
            return
        if(r.status_code == 404):
            await ctx.send("Unknown sample")
            return

        sample = r.content
        if(sample == "Sample not found"):
            await ctx.send("Sample not found")
            return
        if(sample == "Invalid Hash..."):
            await ctx.send("Invalid hash...")
            return
        await ctx.send("One serving of malware coming up, check your private messages in a moment!")
        open(os.path.join(pathToVXCage, arg), "wb").write(sample)
        cmd = [pathTo7z, 'a', (pathToVXCage + arg + "_zipped"), pathToVXCage + arg,  '-pinfected']
        mPath = (pathToVXCage + arg)
        zPath = (pathToVXCage + arg + "_zipped")
        proc = subprocess.Popen(cmd)
        proc.communicate()
        nzPath = zPath + ".7z"
        with open(nzPath, 'rb') as fp:
            await ctx.author.send(file=discord.File(fp, 'Malware.zip'))
        os.remove(nzPath)
        os.remove(mPath)

    @commands.command(name="mssearch")
    async def malshare_hash_search(self, ctx, arg):
        endpoint = "https://malshare.com/api.php/?api_key={}&action=search&query={}".format(malshareApi, arg)
        r = requests.get(endpoint)
        try:
            j_obj = json.loads(r.content)
        except:
            await ctx.send("The sample was not found, or the hash is invalid")
            return
        embed = discord.Embed(title="Malshare hash search", color=0x00ff00)
        embed.add_field(name="File type: ", value=j_obj['type'] or "null", inline=False)
        embed.add_field(name="MD5 hash: ", value=j_obj['md5'] or "null", inline=False)
        embed.add_field(name="Source: ", value=j_obj['source'] or "null", inline=False)
        for hit in j_obj['yarahits']['yara']:
            embed.add_field(name="YARA rule hit: ", value=hit or "null", inline=False)

        for parent in j_obj['parentfiles']:
            embed.add_field(name="Parent file MD5 hash: ", value=parent['md5'] or "null", inline=False)

        for sub in j_obj['subfiles']:
            embed.add_field(name="Sub file MD5 hash: ", value=sub['md5'] or "null", inline=False)

        await ctx.channel.send(embed=embed)









def setup(bot):
    bot.add_cog(MalshareCog(bot))