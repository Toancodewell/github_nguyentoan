from wsgiref.validate import validator
from datetime import datetime as dt
from dotenv import load_dotenv
import os
import pprint
from pymongo import MongoClient 

# password = os.environ.get("Sq4I26sG4P7j7ZYr")
connection_string= "mongodb+srv://nguyenvantoan18112000:Sq4I26sG4P7j7ZYr@cluster0.oomitvr.mongodb.net/?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(connection_string)
production = client.production 
def create_book():
    book_validator= {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["title","authors","publish_date","type","copies"],
            "properties": {
                "title": {
                "bsonType": "string",
                "description": "must be a string and is required"
                },
                "authors": {
                "bsonType": "array",
                "items":{
                    "bsonType": "objectId",
                    "description": "must be a string and is required"
                }
                },
                "publish_date": {
                "bsonType": "date",
                "description": " must be a double if the field exists"
                },
                "type":{
                    "enum":["Fiction","Non-Fiction"],
                    "description":"can only be one of the enum values and is required "
                },
                "copies":{
                    "bsonType":"int",
                    "mininum":0,
                    "description":"must be an integer greater than 0 and is required"

                },
            }
        }
    }
    try:
        production.create_collection("book")   
    except Exception as e:
        print(e)

    production.command("collMod","book",validator=book_validator)

create_book()

def create_author_collection():
   author_validator= {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "first_name", "last_name", "date_of_birth"],
         "properties": {
            "first_name": {
               "bsonType": "string",
               "description": "must be a string and is required"
            },
            "last_name": {
               "bsonType": "string",
               "description": " must be an integer in [ 2017, 3017 ] and is required"
            },
            "date_of_birth": {
               "bsonType": "date",
               "description": "must be a double if the field exists"
            },
         }
      }
   }
   try:
        production.create_collection("author")   
   except Exception as e:
        print(e)    
   production.command("collMod","author",validator=author_validator)

# create_author_collection()

def create_data():
    author =[{
        "first_name":"Tim",
        "last_name":"Ruscica",
        "date_of_birth":dt(2000,7,20)
    },
    {
        "first_name":"George",
        "last_name":"Orwell",
        "date_of_birth":dt(1903,6,25)
    },
    {
        "first_name":"Herman",
        "last_name":"Melville",
        "date_of_birth":dt(1819,9,1)
    },
    {
        "first_name":"F.Scott",
        "last_name":"Fix",
        "date_of_birth":dt(1896,9,24)
    }
    ]
    authors = production.author.insert_many(author).inserted_ids
# create_data()

# books =[{
#     "title":"Moby Dick",
#     "authous":[authors[2]],
#     "publish_date":dt.today(),
#     "type":"Non-Fiction",
#     "copies":5
# }]
# production.book.insert_many(books)