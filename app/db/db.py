from pymongo import MongoClient

url = 'mongodb://localhost:27017'

def get_db():
    return MongoClient(url)['db@1_23']