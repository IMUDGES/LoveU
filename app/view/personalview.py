# -*- coding:utf-8 -*-
from flask import jsonify, request
from app import app
from app.controller.service.nickname import Nickname


@app.route('/nickname', methods = ['POST', 'GET'])
def nickname():
    nicknameq = Nickname()
    form = request.form()
    UserPhone = form.get('UserPhone')
    SecretKey = form.get('SecretKey')
    NickName = form.get('NickName')
    return jsonify(nicknameq.change(UserPhone,SecretKey,NickName))