from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
THRESHOLD = os.getenv("THRESHOLD")
WHITELISTED_IPS = os.getenv("WHITELISTED_IPS")