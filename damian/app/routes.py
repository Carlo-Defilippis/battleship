from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Damian'}
    return render_template('index.html', title='Home', user=user)

def battleship():
    pass
