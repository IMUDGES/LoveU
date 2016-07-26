from app import app
from flask import Flask


@app.route('/')
@app.route('/index')
def index():
    return "HELLO,LOVEU!"
