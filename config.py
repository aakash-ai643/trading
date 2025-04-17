import os
from dotenv import load_dotenv

load_dotenv()  # 🔥 .env File से Keys Load करें

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
EXCHANGE = "binance"
