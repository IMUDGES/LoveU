# -*- coding:utf-8 -*-
from flask import jsonify, request
from app import app
from app.controller.service.nickname import Nickname
from app.controller.jwxtservice.upjwxtservice import upjwxtService


@app.route('/nickname', methods = ['POST', 'GET'])
def nickname():
    nicknameq = Nickname()
    form = request.form()
    UserPhone = form.get('UserPhone')
    SecretKey = form.get('SecretKey')
    NickName = form.get('NickName')
    return jsonify(nicknameq.change(UserPhone, SecretKey, NickName))


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
    JwxtNumber = form.get('JwxtNumber')
    JwxtPassword = form.get('JwxtPassword')
    return "未完成"
