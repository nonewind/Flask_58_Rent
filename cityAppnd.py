'''
Author: Ziheng
Date: 2021-01-11 10:19:48
LastEditTime: 2021-06-06 14:05:26
'''
from pymongo import MongoClient
from config import MONGO


data = {
    "city_task": [
        {
            "city_58": "qd",
            "city_zh": "青岛"
        }, {
            "city_58": "jn",
            "city_zh": "济南"
        }, {
            "city_58": "bj",
            "city_zh": "北京"
        }, {
            "city_58": "sh",
            "city_zh": "上海"
        }, {
            "city_58": "hf",
            "city_zh": "合肥"
        }
    ]
}
print(MONGO)
client = MongoClient(MONGO,connect=False)
db = client["Fuck_58"]
coll = db['spider_task']

coll.insert_one(data)
