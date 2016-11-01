# -*- coding:utf-8 -*-
from flask import jsonify, request, render_template
from app import app
from app.controller.service.nickname import Nickname
from app.controller.jwxtservice.upjwxtservice import upjwxtService
from app.controller.jwxtservice.jwxtservice import JwxtService
from app.controller.jwxtservice.downclass import Downclass


@app.route('/changemydata', methods = ['POST', 'GET'])
def nickname():
    nicknameq = Nickname()
    form = request.form
    UserPhone = form.get('UserPhone')
    SecretKey = form.get('SecretKey')
    NickName = form.get('NickName')
    UserSex = form.get('UserSex')
    return jsonify(nicknameq.change(UserPhone, SecretKey, NickName,UserSex))

@app.route('/upjwxtservice', methods = ['POST', 'GET'])
def upjwxtservice():
    form = request.form
    UserPhone = form.get('UserPhone')
    Secretkey = form.get('SecretKey')
    JwxtNumber = form.get('JwxtNumber')
    JwxtPassword = form.get('JwxtPassword')
    upjwxtserviceinfo = upjwxtService()
    return jsonify(upjwxtserviceinfo.check(UserPhone,Secretkey,JwxtNumber,JwxtPassword))


@app.route('/downclass', methods = ['POST', 'GET'])
def downclass():
    UserPhone = request.args.get('UserPhone')
    Secretkey = request.args.get('SecretKey')
    # UserPhone = '11111111114'
    # Secretkey = '61f70c29fda751350de97e7b92163de4'
    downclassinfo = Downclass()
    n = downclassinfo.downclass(UserPhone,Secretkey)
    return jsonify(n['data'])


@app.route('/selectclass', methods=['POST', 'GET'])
def selectclass():
    form = request.form
    UserPhone = form.get('UserPhone')
    Secretkey = form.get('SecretKey')
    ClassNumber = form.get('ClassNumber')
    ClassOrder = form.get('ClassOrder')
    j = JwxtService()
    return jsonify(j.chooseClass(UserPhone, Secretkey, ClassNumber, ClassOrder))


@app.route('/testclass', methods=['GET'])
def testc():
    UserPhone = request.args.get('UserPhone')
    Secretkey = request.args.get('SecretKey')
    data = {
        'UserPhone': UserPhone,
        'SecretKey': Secretkey
    }
    # # UserPhone = '11111111114'
    # # Secretkey = '61f70c29fda751350de97e7b92163de4'
    # downclassinfo = Downclass()
    # n = downclassinfo.downclass(UserPhone,Secretkey)
    # data = str(n['data'])
    # print(type(data))
    return render_template('index.html', data=data)

