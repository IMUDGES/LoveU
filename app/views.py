from flask import jsonify
from flask import request, render_template

from app import app
from app.bean.secretkey import Secretkey
from db import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
    form = request.form
    UserPhone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    u = User.query.filter_by(UserPhone = UserPhone).first()
    if u is None:
        msg = '0'
        SecretKey = None
    else:
        if u.PassWord == PassWord:
            msg = '1'
            S = Secretkey()
            SecretKey = S.GetSecretKey()
            u.SecretKey = SecretKey
        else:
            msg = '0'
            SecretKey = None
    array = {
        'msg':msg,
        'SecretKey':SecretKey
    }
    return jsonify(array)
@app.route('/food',methods = ['POST', 'GET'])
def food():
    UserPhone = request.args.get('UserPhone')
    Secretkey = request.args.get('SecretKey')
    if Secretkey is not None:
        u = User.query.filter_by(UserPhone = UserPhone).first()
        if u.SecretKey == Secretkey:








