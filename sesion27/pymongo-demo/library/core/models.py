
from django.db import models
from core.lib.db import connect

# Create your models here.

class Book():

    def __init__(self):
        self.db_handle, self.db_client = connect()

    def insert(self, data):
        books_collection=self.db_handle["books_col"]
        books_collection.insert(data)

    def find_by_title(title):
        db_handle, db_client = connect()
        books_collection = db_handle["books_col"]
        books = list(books_collection.find({"title": title}, {"_id": 0}))
        return books
    
    def all():
        db_handle, db_client = connect()
        books_collection = db_handle["books_col"]
        books = list(books_collection.find({}, {"_id": 0}))
        return books

    def search(query):
        db_handle, db_client = connect()
        books_collection = db_handle["books_col"]
        books = list(books_collection.find(query, {'_id': 0}))
        return books