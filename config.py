import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID', 'YOUR_ADMIN_CHAT_ID')
MEDIA_CHANNEL_ID = os.getenv('MEDIA_CHANNEL_ID', 'YOUR_MEDIA_CHANNEL_ID')
WELCOME_VIDEO_ID = os.getenv('WELCOME_VIDEO_ID', None)

ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

POSITIONS = {
    'sales': 'Sotuv menejeri',
    'smm': 'SMM mutaxasisligi',
    'copywriter': 'Kopirayter',
    'volunteer': 'Valantyor'
}

PROXY_URL = os.getenv('PROXY_URL', None)
PROXY_USERNAME = os.getenv('PROXY_USERNAME', None)
PROXY_PASSWORD = os.getenv('PROXY_PASSWORD', None)
