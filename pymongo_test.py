# coding=utf-8

import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.laurence

# collection = db.laurence

ss = db.rhewitt.find_one({"_id": 1.0})

# print ss

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mogodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id

if __name__ == '__main__':
    ss = db.posts.find()
    for i in ss:
        print i["_id"]

    pass
