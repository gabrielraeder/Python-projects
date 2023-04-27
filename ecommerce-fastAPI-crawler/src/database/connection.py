from pymongo import MongoClient

import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST") or "localhost"
DB_PORT = os.getenv("DB_PORT_MONGO") or 27017

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.ecommerce
