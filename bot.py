import os
import nextcord
from nextcord.ext import commands
from flask import Flask
from threading import Thread
from utils.helpers import add_balance, get_balance, add_proof, get_proofs, get_total_balance, update_treasury, get_treasury_balance
import config

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def hello():
    return "Albion Guild Assistance bot is running."

# Initialize the bot
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Add your cogs here
bot.load_extension("cogs.balance")

# Function to run the bot
def run_bot():
    bot.run(config.BOT_TOKEN)

# Function to run the Flask server
def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Create two threads to run both the Flask server and the Discord bot
    flask_thread = Thread(target=run_flask)
    bot_thread = Thread(target=run_bot)

    # Start both threads
    flask_thread.start()
    bot_thread.start()

    # Wait for both threads to complete
    flask_thread.join()
    bot_thread.join()
