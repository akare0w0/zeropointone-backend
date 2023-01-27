from pymongo import MongoClient

url = 'mongodb://localhost:27017'

def get_client() -> MongoClient:
    return MongoClient(url)