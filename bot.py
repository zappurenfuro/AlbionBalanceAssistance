# bot.py
import nextcord
from nextcord.ext import commands
import config
import os
from flask import Flask

# Dummy HTTP server for Render
app = Flask(__name__)

@app.route('/')
def hello():
    return "Albion Guild Assistance bot is running."

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

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
