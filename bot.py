import discord
from discord.ext import commands
from config import discordToken
from pyfiglet import Figlet

bot = commands.Bot(command_prefix="mal ")
bot.remove_command('help')
fig = Figlet(font="Graceful")
cogs = []
cogs.append('cogs.Misc')
cogs.append('cogs.Malshare')
cogs.append('cogs.Threatminer')
cogs.append('cogs.Virustotal')
cogs.append('cogs.URLHAUS')
cogs.append('cogs.HoneyDB')

if __name__ == '__main__':
    for ext in cogs:
        bot.load_extension(ext)
@bot.event
async def on_ready():
    print(fig.renderText("A L E X S I S"))
    print("Ready to assist :)")
    await bot.change_presence(activity=discord.Game(name="with malware 🐲 "))


bot.run(discordToken)
