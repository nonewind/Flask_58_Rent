from pymongo import MongoClient


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

client = MongoClient('mongodb://101.32.185.181:27017',connect=False)
db = client["Fuck_58"]
coll = db['spider_task']

coll.insert(data)
