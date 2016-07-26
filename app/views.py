from app import app
from flask import Flask, jsonify
from flask import request, render_template, url_for
from secretkey import Secretkey
from db import User
import db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
    form = request.form
    UserPhone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    u=User.query.filter_by(UserPhone=UserPhone).first()
    if u is None:
        msg='0'
        SecretKey=None
    else:
        if u.PassWord == PassWord:
            msg='1'
            S=Secretkey()
            SecretKey=S.GetSecretKey()
            u.SecretKey=SecretKey
        else:
            msg='0'
            SecretKey=None
    array={
        'msg':msg,
        'SecretKey':SecretKey
    }
    return jsonify(array)




