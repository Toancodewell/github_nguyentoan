from dotenv import load_dotenv
import os
import pprint
from pymongo import MongoClient 

client = MongoClient('mongodb://localhost:27017/')
test_db = client.bookstore
collections = test_db.list_collection_names()
# print(collections)

def insert_test_doc():
    collection = test_db['test']
    test_document = {
        "name":"Tim",
        "type":"Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)
# insert_test_doc()

production = client.production 
person_collection = production.person_collection 

def create_documents():
    first_names =["Tim","Sarah","Jennider","Jose","Brad","Allen"]
    last_names =["Ruscica","Smith","Bart","Cater","Pit","Geral"]
    ages = [21,40,23,19,34,67]

    docs=[]

    for first_name , last_name, age in zip(first_names, last_names,ages ):
        doc = {"first_name":first_name,"last_name":last_name,"age":age}
        docs.append(doc)
    person_collection.insert_many(docs)
# create_documents()

# for x in person_collection.find():
#     print(x)
printer = pprint.PrettyPrinter()

def find_all_people():
    for x in person_collection.find():
        printer.pprint(x)
# find_all_people()

# print(person_collection.count_documents({}))

# for x in person_collection.find({"$and":[{"age":{"$gte":20}},{"age":{"$lte":35}}]}).sort("age"):
#     print(printer.pprint(x))

# giu id thay noi dung ben trong.
def replace_one(person_id):
    from bson.objectid import ObjectId 
    _id = ObjectId(person_id)

    new_doc ={
        "firts_name":"new first name",
        "last_name":"new last name",
        "age":80
        }
    person_collection.replace_one({"_id":_id},{new_doc})


# 
address={
    "_id":"64b21fa74e5295cdb7b3661a",
    "street":" Bay Street",
    "number":2706,
    "city":"San"
}
def add_address_relationship(person_id,address):
    address_collection = production.address 
    address_collection.insert_one(address)

add_address_relationship('64b21fa74e5295cdb7b36619',address)

