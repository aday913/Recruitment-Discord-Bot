import os
import random

from discord import errors
from discord.ext import commands
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

# @bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
# async def nine_nine(ctx):
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]

#     response = random.choice(brooklyn_99_quotes)
#     await ctx.send(response)

print('Attempting to log in the bot...')
try:
    bot.run(TOKEN)
except errors.LoginFailure:
    print('The bot could not log in, check the token!')