from socket import TCP_NODELAY
from pymongo import MongoClient 
# url ="mongodb+srv://nguyenvantoan18112000:QxvvlWiOWpDZW74e@cluster0.oomitvr.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("mongodb+srv://nguyenvantoan18112000:OKfXYgC2KQT70NFr@cluster0.oomitvr.mongodb.net/?retryWrites=true&w=majority")
db=client.test 


# mydict = { "name": "John", "address": "Highway 37" }
# x = db.todays.insert_one(mydict)# x= collection.insert_one()

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

db.todays.insert_many(mylist)
