from app import app
from flask import render_template,jsonify

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
        'rents.html',
        title = '我在等你回家'
    )