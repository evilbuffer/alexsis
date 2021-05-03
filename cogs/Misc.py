import discord
from discord.ext import commands
from config import ownerId
class MiscCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='echo')
    async def echo(self, ctx, *, input: str):
        await ctx.send(input)

    @commands.command(name='nuke')
    async def purge(self, ctx, arg : int):
        channel = ctx.channel
        if(ctx.message.author.id == ownerId):
            if(arg == 69):
                await channel.purge(limit=None)
            else:
                await channel.purge(limit=arg)

    @commands.command(name='menu')
    async def menu(self, ctx):
        embed = discord.Embed(title="Awesome help menu", color=0xff6600)
        embed.add_field(name="Prefix", value="Alexsis uses 'mal<space>' as a prefix", inline=False)
        embed.add_field(name="vtdetections", value="Use this command to check Virustotal detections, usage: mal vtdetections <hash>", inline=False)
        embed.add_field(name="vturlcheck", value="Use this command to check if a site is used for malicious purposes, usage: mal vturlcheck <url>", inline=False)
        embed.add_field(name="tmdetection", value="Same as the Virustotal command, but uses Threatminer's DB, usage: mal tmdetection <hash>", inline=False)
        embed.add_field(name="hosts", value="This command returns any known hosts from the hash, usage: mal hosts <hash> ", inline=False)
        embed.add_field(name="tmfileinfo", value="tmfileinfo returns any details from Threatminer's DB about the file, usage: mal tmfileinfo <hash>", inline=False)
        embed.add_field(name="APT", value="Returns any notes regarding APT's, usage: mal APT <query>", inline=False)
        embed.add_field(name="25fresh", value="Returns the 25 newest active malware urls from URL Haus, usage: mal 25fresh", inline=False)
        embed.add_field(name="25md5", value="Returns the 25 newest hashes from Malshare, usage: mal 25md5", inline=False)
        embed.add_field(name="gettypes", value="Gets the amount of different uploaded file types from Malshare, usage: mal gettypes ", inline=False)
        embed.add_field(name="getmalware", value="Downloads the specified hash from Malshare(password for zip is 'infected', usage: mal getmalware <hash>", inline=False)
        embed.add_field(name="mssearch", value="Searches the given hash on Malshare, usage: mal mssearch <hash>", inline=False)
        embed.add_field(name="findmalware", value="Lets you search URL haus for any malware and their according url , usage: mal findmalware <query>", inline=False)
        embed.add_field(name="findurl", value="Lets you search URL haus for any URL, and its according malware, usage: mal findurl <url>", inline=False)
        embed.add_field(name="honeytwitter", value="Returns a txt file with the latest IOC's(IPS) from Twitter", inline=False)
        embed.add_field(name="honeytwittersearch", value="Lets you search an IP on Twitter", inline=False)
        embed.add_field(name="honeyservices", value="Returns the latest HoneyDB services under attack, and count of attacks", inline=False)
        
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(MiscCog(bot))