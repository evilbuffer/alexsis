# Alexsis
## A bot designed to assist with malware analysis.
Alexsis is a quick and dirty bot made with Python and love, meant to make it easier to perform various kinds of malware analysis, and more fun!

## Requirements
* Malshare API key
* Virustotal API key
* Discord bot token
* A config.py in the same path as bot.py, with the following variables
	* discordToken = <your_token>
	* malshareApi = <your_key>
	* virustotalApi = <your_key>
	* pathTo7z = <path_to_7zip_exe>
	* pathToVxCage = <path_to_malware_folder>
	* ownerId = <your_discord_id>
	
## Installation
Currently the bot is meant to be run on Windows, but by replacing the paths, and getting a linux version of 7zip (or using tar) its possible to run it on Linux \
To install simply do
```
git clone https://github.com/pynox/Alexsis.git
cd Alexsis
pip install -r requirements.txt
py bot.py
```
Remember to add the config.py file in the same directory as bot.py, with the required values.

## Usage
Alexsis uses "mal [space]" as a prefix. \
To get a list of available commands 
```
mal menu
```

## Todo
* Create better command names
* Add functionality to analyse EXE files, using modules like PeFile
* YARA functionality? 
* Linux version? 
* New prefix
## WARNING
The bot includes functionality to download real malware, which it will store on whatever computer/server you run the bot from.
So be careful, and don't run the bot on your personal home computer, get a dedicated VPS. \
To be extra safe, run the command in icalc.txt on the folder you want to use as a temporary folder for malware

