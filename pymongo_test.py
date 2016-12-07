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
# posts_1 = db.posts_1
# xx = posts_1.insert_one(post).inserted_id

news_posts = [{
    "author": "Mike",
    "text": "Another post!",
    "tages": ["bulk", "insert"],
    "date": datetime.datetime.utcnow()
},
    {"author": "Eliot",
     "title": "MongoDB is fun",
     "text": "and pretty easy too!",
     "date": datetime.datetime.utcnow()

     }
]

blog_dic={'content': u'\r\n\r\n<h2><strong>find_one:</strong></h2>&#13;\n<p>hos_dep_list = db.hospital_general.find_one({"_id": ObjectId(id)})<br />&#13;\nkk = type(hos_dep_list)</p>&#13;\n<p>\u6d4b\u8bd5\u5f97\u5230\uff1a</p>&#13;\n<p><img src="http://img.blog.csdn.net/20160718103015846" alt="" /><br />&#13;\n</p>&#13;\n<p>\u6545find_one\u67e5\u627e\u5f97\u5230\u7684\u662f\u4e00\u4e2a\u5b57\u5178\uff0c\u56e0\u6b64\u6211\u4eec\u53ef\u4ee5\u76f4\u63a5\u5728\u5176\u540e\u8ddf["key"]\u503c\u5f97\u5230\u6211\u4eec\u60f3\u8981\u7684value\uff0cvalue\u53ef\u4ee5\u662f\u5b57\u7b26\u4e32\uff0c\u53ef\u4ee5\u662f\u5b57\u5178\u4e5f\u53ef\u4ee5\u662flist\uff0c\u8fd9\u6837\u53ef\u4ee5\u65b9\u4fbf\u540e\u7eed\u7684\u5904\u7406\u3002</p>&#13;\n<p>\u4f8b\uff1a</p>&#13;\n<p>hos_dep_list = db.hospital_general.find_one({"_id": ObjectId(id)})["depart"]<br />&#13;\n</p>&#13;\n<h2><strong>find:</strong></h2>&#13;\n<div>hos_dep_list = db.hospital_general.find({"_id": ObjectId(id)})<br />&#13;\nkk = type(hos_dep_list)<br />&#13;\n</div>&#13;\n<div>\u6d4b\u8bd5\u5f97\u5230\uff1a</div>&#13;\n<div><img src="http://img.blog.csdn.net/20160718103524368" alt="" /><br />&#13;\n</div>&#13;\n<div><br />&#13;\n</div>&#13;\n<div>\u53ef\u4ee5\u770b\u5230find\u67e5\u627e\u5f97\u5230\u7684\u662f\u4e00\u4e2a\u6e38\u6807\u3002\u5982\u679c\u4ecd\u50cffind_one\u65f6\u90a3\u6837\u8fdb\u884c\u5982\u4e0b\u64cd\u4f5c</div>&#13;\n<div>hos_dep_list = db.hospital_general.find({"_id": ObjectId(id)})["depart"]<br />&#13;\n</div>&#13;\n<div>\u5219\u4f1a\u62a5\u9519\uff1a</div>&#13;\n<div><img src="http://img.blog.csdn.net/20160718103904951" alt="" /><br />&#13;\n</div>&#13;\n<div><br />&#13;\n</div>&#13;\n<div><br />&#13;\n</div>&#13;\n   &#13;\n', 'cat': u'python \uff084\uff09 mongodb \uff081\uff09', 'tag': 'python pymongo web', 'time': '2016-07-18 10:27', 'title': u'pymongo\u4e2dfind_one\u548cfind\u7684\u533a\u522b'}
blog = db.blog
yy = blog.insert_one(blog_dic).inserted_id

if __name__ == '__main__':
    # result = db.posts.insert_many(news_posts)
    # print db.inserted_ids
    # print db.posts.count()
    # for post in db.posts.find():
    #     print post

    pass
