import os
import nextcord
from nextcord.ext import commands
from keep_alive import keep_alive
import config

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
guilds_ids = []

# Load cogs
initial_extensions = ['cogs.balance']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

    keep_alive()
    bot.run(config.BOT_TOKEN)
    