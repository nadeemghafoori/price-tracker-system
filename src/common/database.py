import pymongo

class Database(object):
    # it means that where the database is located in
    URI = "mongodb://<your-database-host>:27017"
    DATABASE = None                     # when we initialize the database, then we should take it as a none

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)          #client has access to all databases
        Database.DATABASE = client['FinalProject']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)
