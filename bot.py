# bot.py
import nextcord
from nextcord.ext import commands
import config

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs
initial_extensions = ['cogs.balance']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    for guild in bot.guilds:
        print(f'Connected to guild: {guild.name} (ID: {guild.id})')

bot.run(config.BOT_TOKEN)
