from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html'
    )

@app.route('/rents')
def rents():
    return render_template(
        "rents.html",
        title = '快点回家'
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

@app.route('/joinin')
def joinin():
    return render_template(
        'joinin.html',
        title = '少年我看你骨骼精奇...'
    )