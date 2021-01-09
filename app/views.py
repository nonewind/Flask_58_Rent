from app import app
from flask import render_template, request
from pymongo import MongoClient
import json

# 数据库地址 mongoDB server connect
client = MongoClient(app.config["MONGO"], connect=False)
db = client["Fuck_58"]


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html'
    )


@app.route('/rents')
def rents():
    return render_template(
        'rents.html'
    )


@app.route("/more")
def more():
    return render_template(
        'more.html'
    )


@app.route("/rentsData", methods=['POST'])
def rentsData():
    coll = db['spider_result']
    """
    mongoDB中
    1,2 代表0-1k 对应前端 0
    3,4 代表1-2k 对应前端 1
    5,6 代表2-3k 对应前端 2
    """
    cityname = request.args.get("city")  # return like "青岛"
    # 这里不需要验证城市名称 这个名称是由高德查询返回的
    price_level = int(request.args.get("level"))
    list_return = []
    if price_level == 0:
        list_data = []
        data_0 = coll.find({"cityname": cityname, "priceLevel": 1})
        list_data.extend(data_0)
        data_1 = coll.find({"cityname": cityname, "priceLevel": 2})
        list_data.extend(data_1)
    elif price_level == 1:
        list_data = []
        data_0 = coll.find({"cityname": cityname, "priceLevel": 3})
        list_data.extend(data_0)
        data_1 = coll.find({"cityname": cityname, "priceLevel": 4})
        list_data.extend(data_1)
    else:
        list_data = []
        data_0 = coll.find({"cityname": cityname, "priceLevel": 5})
        list_data.extend(data_0)
        data_1 = coll.find({"cityname": cityname, "priceLevel": 6})
        list_data.extend(data_1)

    for line in list_data:
        oo_data = {
            "title": line['title'],
            "url": line["url"],
            "price": line["price"]
        }
        list_return.append(oo_data)
    return({
        "data": list_return
    })


@app.route("/seachCity", methods=['GET'])
def seachCity():
    """
    查询数据库
    返回是否已经支持
    """
    coll = db['spider_task']
    WananCity = request.args.get("city").replace("市", "")
    data = coll.find()[0]["city_task"]
    for line in data:
        if line["city_zh"] in WananCity:
            return("查询成功 已经支持了您查询的城市!")
    return("查询成功 暂时还不支持您查询的城市 您可以提交所查询的城市!")


@app.route("/appendCity", methods=['GET'])
def appendCity():
    city = request.args.get("city").replace("市", "")
    """
    添加到本地文件中
    没事的时候去看看文件中最多的城市是哪个 加到数据库就可以
    算是一个安慰剂效应
    """
    with open("IwananCity.txt", 'a', encoding='utf8') as ff:
        ff.write(city)
        ff.write("\n")
    return("提交成功 感谢您对我的支持!")

# 404 页面 不知道为什么不生效


@app.errorhandler(404)
def page_not_found():
    return ("""
    <h1>Page Not Found</h1>
  <p>What you were looking for is just not there.
  <p><a href="/index">go somewhere nice</a>
    """)
