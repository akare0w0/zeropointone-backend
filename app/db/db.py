from pymongo import MongoClient

url = 'mongodb://6.tcp.cpolar.top:11004';

def get_client() -> MongoClient:
    return MongoClient(url)