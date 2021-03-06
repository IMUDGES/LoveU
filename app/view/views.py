# -*- coding:utf-8 -*-
from flask import jsonify
from flask import request, render_template
from app import app
from app.controller.service.register1 import Register1
from app.controller.service.register2 import Register2
from app.controller.service.register3 import Register3
from app.controller.service.retrieve1 import Retrieve1
from app.controller.service.retrieve2 import Retrieve2
from app.controller.service.retrieve3 import Retrieve3
from app.controller.service.login import dologin
from app.controller.service.data import data
from app.controller.service.searchservice import search

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/login', methods=['POST'])
def login():
    return jsonify(dologin())

#注册模块-----------------------------------------------注册模块
@app.route('/register1', methods=['POST'])
def register1():
    form = request.form
    UserPhone = form.get('UserPhone')
    register1 = Register1()
    return jsonify(register1.register1(UserPhone))


@app.route('/register2', methods=['POST'])
def register2():
    form = request.form
    UserPhone = form.get('UserPhone')
    CheckCode = form.get('CheckCode')
    register2q = Register2()
    return jsonify(register2q.register2(UserPhone, CheckCode))


@app.route('/register3', methods=['POST'])
def register3():
    form = request.form
    UserPhone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    NickName = form.get('NickName')
    CheckCode = form.get('CheckCode')
    register2q = Register2()
    array = register2q.register2(UserPhone, CheckCode)
    q = int(array['state'])
    if q == 1:
        register3 = Register3()
        print(array)
        return jsonify(register3.register3(UserPhone, PassWord, NickName))
    else:
        print(array)
        return jsonify(array)
# 注册模块结束-----------------------------------------------注册模块结束


@app.route('/data', methods = ['POST', 'GET'])
def getdata():
    UserId = int(request.args.get('UserId'))
    d = data()
    return jsonify(d.Get_OthersData(UserId))


@app.route('/mydata', methods = ['POST', 'GET'])
def mydata():
    d = data()
    return jsonify(d.GetMyData())


#找回密码模块-----------------------------------------------找回密码模块
@app.route('/retrieve1', methods=['POST'])
def retrieve1():
    form = request.form
    UserPhone = form.get('UserPhone')
    retrieve1q = Retrieve1()
    return jsonify(retrieve1q.retrieve1(UserPhone))


@app.route('/retrieve2', methods=['POST'])
def retrieve2():
    form = request.form
    UserPhone = form.get('UserPhone')
    CheckCode = form.get('CheckCode')
    retrieve2q = Retrieve2()
    return jsonify(retrieve2q.Retrieve2(UserPhone, CheckCode))


@app.route('/retrieve3', methods=['POST'])
def retrieve3():
    form = request.form
    UserPhone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    CheckCode = form.get('CheckCode')
    retrieve2q = Retrieve2()
    retrieve3q = Retrieve3()
    array = retrieve2q.Retrieve2(UserPhone, CheckCode)
    q = int(array['state'])
    if q == 1:
        retrieve3q = Retrieve3()
        return jsonify(retrieve3q.retrieve3(UserPhone, PassWord))
    else:
        return jsonify(array)

#找回密码模块结束-----------------------------------------------找回密码模块结束

# 查询
@app.route('/searchall', methods=['GET', 'POST'])
def searchall():
    s = search()
    message = request.args.get('Message')
    if message is not None:
        return jsonify(s.searchall(message))
    else:
        array = {
            'state': 0,
            'msg': '查询失败'
        }
        return jsonify(array)
#end

