import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
GUILD_IDS = list(map(int, os.getenv('GUILD_IDS', '').split(','))) if os.getenv('GUILD_IDS') else []
ALLOWED_USER_ID = int(os.getenv('ALLOWED_USER_ID', '0'))
