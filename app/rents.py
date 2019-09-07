from app import app
from flask import render_template

@app.route('/rents')

def rents():
    return render_template(
        "rents.html"
    )