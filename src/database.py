from pymongo import MongoClient
from pymongo.database import Database
from src.config import settings

client = MongoClient(settings.DATABASE_URL)
db = client.get_database(name='alpha')

def get_db() -> Database:
    return db

# Optional: Function to close the connection
def close_mongo_connection():
    client.close()