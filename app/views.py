from app import app
from flask import render_template,jsonify
import sqlite3

DATABASE = 'D:\CODE/flask_text/app.db'

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html'
    )

@app.route('/city')
def city():
    return render_template(
        "city.html",
        title = '支持的城市列表'
    )

@app.route('/about')
def about():
    return render_template(
        "About.html",
        title = '嘿嘿嘿...其实我是...'
    )

@app.route('/help')
def help():
    return render_template(
        'help.html',
        title = '救救孩子吧...'
    )

@app.route('/rents')
def rents():
    return render_template(
        'rents.html'
    )

@app.route('/rents/<name>',methods=['GET'])
def rents_test(name):
    sqlite3DB = sqlite3.connect(DATABASE)
    if name == '0':
        cur = sqlite3DB.execute("select QingDao_00 from Location")
        curss = cur.fetchall()
    else:
        return '数据库报错?????'

    sqlite3DB.close()
    curss_list = ''
    for i in curss:
        i = str(i)
        i = i.replace("('","")
        i = i.replace("',)",'')
        curss_list = curss_list+i+','
    return render_template(
        'rents.html',
        name = curss_list
    )