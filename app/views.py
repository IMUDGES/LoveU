# -*- coding:utf-8 -*-
from flask import jsonify
from flask import request, render_template
from app import app
from app.bean.secretkey import Secretkey
from app.db import User
from app.controller.service.register2 import Register2
from app.controller.service.register3 import Register3
from app.controller.service.sendmessage import SendMessage
from app.controller.service.login import dologin
from app.controller.foodservice.food import foodservice
from app.controller.service.data import data
from app.controller.jwxtservice.upjwxtservice import upjwxtService
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')


@app.route('/login', methods=['POST'])
def login():
    return jsonify(dologin())


@app.route('/register1', methods=['POST'])
def register1():
    form = request.form
    UserPhone = form.get('UserPhone')
    sendMessage = SendMessage()
    sendMessage.sendmessage(UserPhone)
    state = 1
    msg = "成功"
    array = {
        'state':state,
        'msg': msg,
    }
    return jsonify(array)


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
    q = int(array['msg'])
    if q == 1:
        register3 = Register3()
        return jsonify(register3.register3(UserPhone, PassWord, NickName))
    else:
        return jsonify(array)


@app.route('/food', methods = ['POST', 'GET'])
def food():
    f = foodservice()
    return jsonify(f.food())


@app.route('/creatfood', methods = ['POST', 'GET'])
def creatfood():
    f = foodservice()
    return jsonify(f.creat())


@app.route('/getfood', methods=['POST', 'GET'])
def getfood():
    f = foodservice()
    return jsonify(f.get())


@app.route('/canclefood', methods = ['POST', 'GET'])
def canclefood():
    f = foodservice()
    return jsonify(f.cancle())


@app.route('/myfood', methods = ['POST', 'GET'])
def myfood():
    f = foodservice()
    return jsonify(f.myfood())


@app.route('/thisfood', methods = ['GET', 'POST'])
def thisfood():
    f= foodservice()
    return jsonify(f.thisfood())


@app.route('/data', methods = ['POST', 'GET'])
def getdata():
    d = data()
    return jsonify(d.GetOthersData())


@app.route('/mydata', methods = ['POST', 'GET'])
def mydata():
    d = data()
    return jsonify(d.GetMyData())


@app.route('/test')
def test():
    #test 如果不用 记得删掉
    u = User.query.filter_by(UserPhone='18548186741').first()
    print (u.NickName)
    return u.NickName

@app.route('/upjwxtservice', methods = ['POST', 'GET'])
def upjwxtservice():
    form = request.form
    UserPhone = form.get('UserPhone')
    Secretkey = form.get('SecretKey')
    JwxtNumber = form.get('JwxtNumber')
    JwxtPassword = form.get('JwxtPassword')
    upjwxtserviceinfo = upjwxtService()
    return jsonify(upjwxtserviceinfo.check(UserPhone,Secretkey,JwxtNumber,JwxtPassword))

@app.route('/run', methods=['POST','GET'])
def run():
    #此模块未完成
    pass