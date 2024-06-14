import os
import nextcord
from nextcord.ext import commands
from flask import Flask
import asyncio

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def hello():
    return "Albion Guild Assistance bot is running."

# Initialize the bot
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Load your cogs here
bot.load_extension("cogs.balance")

async def run_bot():
    await bot.start(os.environ.get('BOT_TOKEN'))

async def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

async def main():
    bot_task = asyncio.create_task(run_bot())
    flask_task = asyncio.create_task(run_flask())
    await asyncio.gather(bot_task, flask_task)

if __name__ == "__main__":
    asyncio.run(main())
