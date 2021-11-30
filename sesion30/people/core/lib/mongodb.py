from pymongo import MongoClient

def connect():
    client = MongoClient("mongodb+srv://root:rootcodigo@cluster0.ppe0h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db_handle = client['PeopleDB']
    return db_handle, client