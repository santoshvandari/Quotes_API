from pymongo import MongoClient

MONGO_URI='<Insert your MongoDB URI>'

# connect to the database pymongo 
try:
    client = MongoClient(MONGO_URI)
    db = client.get_database('quotes')
    print('Connected to the database')
except Exception as e:
    print(f'Error connecting to the database: {e}')
    client = None
    exit(1)
