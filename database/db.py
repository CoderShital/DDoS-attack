from pymongo import MongoClient
from config import MONGO_URL, DATABASE_NAME

client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]

traffic_collection = db["traffic_logs"]
blocked_collection = db["blocked_ips"]
whitelisted_collection = db["whitelisted_ips"]


