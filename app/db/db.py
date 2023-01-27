from pymongo import MongoClient

url = 'mongodb://jp-tyo-ntt-1.natfrp.cloud:16412';

def get_client() -> MongoClient:
    return MongoClient(url)