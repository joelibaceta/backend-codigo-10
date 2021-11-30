from django.db import models
from core.lib.mongodb import connect

# Create your models here.
class Person():

    db_handle, db_client = connect()

    def insert(data):
        people_collection = Person.db_handle["people_col"]
        people_collection.insert(data)
        result = data.pop("_id", None)
        return result


    
