from app import app
from flask import render_template, jsonify
import sqlite3

DATABASE = 'D:\CODE/flask_text/data_loc.db'


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html'
    )


@app.route('/help')
def help():
    return render_template(
        'help.html',
        title='救救孩子吧...'
    )


@app.route('/rents')
def rents():
    return render_template(
        'rents.html'
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
        page = page_number
    )
