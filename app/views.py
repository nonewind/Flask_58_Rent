from app import app
from flask import render_template, request
import sqlite3
from pymongo import MongoClient

# 数据库地址 mongoDB server connect
client = MongoClient('mongodb://TaapSpider:mongouser@mongodb01.tools/login')
db = client["Taotie"]
coll = db["test_Spider_EXP_B"]

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
    cityname = request.args.get("city")
    price_level = request.args.get("level")
    print(cityname, price_level)
    data = {
        "msg":"ok",
        "data":[{"title":"台柳路附近，照片实图精装朝南主卧独卫特价出租免中介","url":"xxxxxxxxxxxxx"},
        {"title":"伊春路附近，照片实图精装朝南主卧独卫特价出租免中介","url":"xxxxxxxxxxxxx"},
        {"title":"台湛路附近，照片实图精装朝南主卧独卫特价出租免中介","url":"xxxxxxxxxxxxx"}]
        }
    return(data)


@app.route("/seachCity", methods=['GET'])
def seachCity():
    WananCity = request.args.get("city")
    """
    查询数据库
    返回是否已经支持
    """
    return(WananCity)


@app.route("/appendCity", methods=['GET'])
def appendCity():
    city = request.args.get("city")
    """
    添加到本地文件中
    没事的时候去看看文件中最多的城市是哪个 加到数据库就可以
    算是一个安慰剂效应
    """
    return(city)

# 404 页面 不知道为什么不生效
@app.errorhandler(404)
def page_not_found():
    return ("""
    <h1>Page Not Found</h1>
  <p>What you were looking for is just not there.
  <p><a href="/index">go somewhere nice</a>
    """)
