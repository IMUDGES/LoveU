from app import app
from flask import Flask,jsonify
from flask import request,render_template,url_for
from db import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    form = request.form
    userphone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    print userphone
    print PassWord
    if not userphone:
        return '0'
    else:
        if not PassWord:
            return '2'
        else:
            u=User.query.filter_by(UserPhone=userphone).first()
            if u.PassWord == PassWord:

                return '1'
            else:
                return '3'




