import os
import random
import json

with open("studentSchedules.json", "r") as f:
    schedules = json.load(f)

recruitNames = []
for key in schedules:
    recruitNames.append(key)

from discord import errors
from discord.ext import commands
from discord import utils
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='socials', help='Responds with links to the various BME social media sites')
async def socialLinks(ctx):
    socialMediaLinks = (
            'Follow the UA BME department at the following social media links!\n'
            'Insta: https://www.instagram.com/uarizonabme/?hl=en \n'
            'Twitter: https://twitter.com/uarizonabme?lang=en'
        )
    
    await ctx.send(socialMediaLinks)

@bot.command(name='github', help='Provides a link to the Discord server bot source code')
async def github(ctx):
    githubLink = (
            'Interested in how this bot functions? Head over to the github repository containing the source code below: \n'
            'Github: https://github.com/aday913/Recruitment-Discord-Bot'
        )

    await ctx.send(githubLink)

@bot.command(name='schedule', help="Provides an overall schedule if no recruit name is provided, otherwise will provide a certain recruit's schedule")
async def getSchedules(ctx, name=None):
    print(ctx.author)
    responseText = [
        '8:00 - 10:00: Welcome\n',
        '10:00 - 11:00: Data Blitz\n',
    ]
    if name in recruitNames:
        responseText.append(schedules[name])
    else:
        responseText.append('GENERIC RESPONSE')
    response = ''
    await ctx.send(response.join(responseText))

@bot.command(name='createTextChannel', help='Will create a text channel if a user with admin privileges wants to')
@commands.has_role('admin')
async def createTextChannel(ctx, channelName):
    guild = ctx.guild
    existing_channel = utils.get(guild.channels, name=channelName)
    if not existing_channel:
        await guild.create_text_channel(channelName)

@bot.command(name='createVoiceChannel', help='Will create a voice channel if a user with admin privileges wants to')
@commands.has_role('admin')
async def createVoiceChannel(ctx, channelName):
    guild = ctx.guild
    existing_channel = utils.get(guild.channels, name=channelName)
    if not existing_channel:
        await guild.create_voice_channel(channelName)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

print('Attempting to log in the bot...')
try:
    bot.run(TOKEN)
except errors.LoginFailure:
    print('The bot could not log in, check the token!')