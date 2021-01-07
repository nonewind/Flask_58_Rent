from app import app
from flask import render_template, request
import sqlite3


DATABASE = 'data_loc.db'


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
    return('{"xx":"台柳路附近，照片实图精装朝南主卧独卫特价出租免中介  "}')


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
