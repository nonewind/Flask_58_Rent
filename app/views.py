'''
Author: Ziheng
Date: 2021-01-11 10:19:48
LastEditTime: 2021-06-06 16:43:57
'''
from threading import excepthook
from pymongo.message import insert
from app import app
from flask import render_template, request, redirect, url_for
from pymongo import MongoClient
import json

# 数据库地址 mongoDB server connect
client = MongoClient(app.config["MONGO"], connect=False)
db = client["Fuck_58"]
""" with open("tt.json",'r',encoding='utf8') as ff:
    data_json = json.loads(ff.read())
print(len(data_json['data'])) """


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/rents')
def rents():
    return render_template('rents.html')


@app.route("/more")
def more():
    return render_template('more.html')


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
        oo_data = {"title": line['title'], "url": line["url"], "price": line["price"],"img":line["img"],"class":line["class"],"from":line['from']}
        list_return.append(oo_data)

    return ({"data": list_return})


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
            return ("查询成功 已经支持了您查询的城市!")
    return ("查询成功 暂时还不支持您查询的城市 您可以提交所查询的城市!")


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
    return ("提交成功 感谢您对我的支持!")


@app.route("/login", methods=['POST'])
def login():
    user = request.args.get("user")
    pass_word = request.args.get("pass")
    """
    查询数据库
    """
    return "success"


@app.route("/admin", methods=['GET'])
def admin():
    try:
        user = request.args.get("user")
        if user:
            return render_template("admin.html")
        else:
            return render_template("login.html")
    except:
        return render_template("login.html")


@app.errorhandler(404)
def page_not_found(xx):
    return ("""
    <script type="text/javascript" src="//qzonestyle.gtimg.cn/qzone/hybrid/app/404/search_children.js" charset="utf-8" homePageUrl="index" homePageName="回到我的主页"></script>
    """)


@app.errorhandler(500)
def page_not_found(xx):
    return ("""
    <script type="text/javascript" src="//qzonestyle.gtimg.cn/qzone/hybrid/app/500/search_children.js" charset="utf-8" homePageUrl="index" homePageName="回到我的主页"></script>
    """)


@app.route("/admin_push", methods=['POST', "GET"])
def admin_push():
    # 切换到任务表
    coll = db['spider_task']
    try:
        data = request.args.get("data")
        class_data = str(request.args.get("class"))
    except:
        return {"msg": "error!数据不全"}
    try:
        data_push = json.loads(data)
    except:
        return {"msg": "error!检查格式"}
    if class_data == "0":
        # 0 : 增加  1: 删除
        oo = coll.find()
        for line in oo:
            ppp = line['city_task']
        try:
            for line in ppp:
                if line == data_push:
                    return {"msg": "error!库内已有该城市"}
        except:
            return {"msg": "数据库错误 请检查数据库数据"}
        ppp.append(data_push)
        data_inset = {"city_task": ppp}
        coll.drop()
        coll.insert_one(data_inset)
        return {"msg": "添加成功"}
    elif class_data == "2":
        oo = coll.find()
        for line in oo:
            ppp = line['city_task']
        return {"msg": ppp}
    else:
        oo = coll.find()
        for line in oo:
            ppp = line['city_task']
        insert_data = []
        try:
            for line in ppp:
                if line != data_push:
                    insert_data.append(line)
        except:
            return {"msg": "数据库错误 请检查数据库数据"}
        if len(insert_data) == len(ppp):
            return {"msg": "error!库内没有该城市"}
        else:
            data_inset = {"city_task": insert_data}
            coll.drop()
            coll.insert_one(data_inset)
            return {"msg": "删除成功"}
