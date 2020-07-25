from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:test@blocktrade-mkmqt.mongodb.net/test?retryWrites=true&w=majority")

block = client.get_database("blockchain")
users_collection = block.get_collection("transaction")

def save_block(id,tstamp,transaction,prevhash,chash):
    users_collection.insert_one({'_id':id,'tstamp':tstamp,'transaction':transaction,'prevhash':prevhash,'hash':chash})