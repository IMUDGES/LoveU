# -*- coding:utf-8 -*-
from flask import jsonify, request
from app import app
from app.controller.service.nickname import Nickname
from app.controller.jwxtservice.upjwxtservice import upjwxtService
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
    form = request.form
    UserPhone = form.get('UserPhone')
    Secretkey = form.get('SecretKey')
    downclassinfo = Downclass()
    n = downclassinfo.downclass(UserPhone,Secretkey)
    return jsonify(n)
