from app import app
from flask import render_template,request
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


@app.route('/rents/<name>', methods=['GET'])
def rents_test(name):
    sqlite3DB = sqlite3.connect(DATABASE)
    if name == '0':
        cur = sqlite3DB.execute("select * from QingDao_0")
        curss = cur.fetchall()
    elif name == '1':
        cur = sqlite3DB.execute("select * from QingDao_1")
        curss = cur.fetchall()
    elif name == '2':
        cur = sqlite3DB.execute("select * from QingDao_2")
        curss = cur.fetchall()
    else:
        return "The Page 404 ! "
    page_number = int(name) + 2
    sqlite3DB.close()
    curss_list = ''
    for i in curss:
        i = str(i)
        i = i.replace("('", "")
        i = i.replace("',)", '')
        curss_list = curss_list+i+','
    return render_template(
        'rents.html',
        name=curss_list,
        page=page_number
    )

@app.route('/getCityList',methods=['GET'])
def getCityList():
    #要求只返回十个
    return(str(['上海','广东','深圳','重庆','广东','深圳','重庆','广东','深圳','重庆','...']))

@app.route("/seachCity",methods=['GET'])
def seachCity():
    WananCity = request.args.get("city")
    """
    查询数据库
    返回是否已经支持
    """
    return(WananCity)

@app.route("/appendCity",methods=['GET'])
def appendCity():
    city = request.args.get("city")
    """
    添加到本地文件中
    没事的时候去看看文件中最多的城市是哪个 加到数据库就可以
    算是一个安慰剂效应
    """
    return(city)
