# -*- coding:utf-8 -*-
from app.controller.service.mineservice import mine
from flask import jsonify
from app import app
from flask import request


@app.route('/mine')
def MINEDATA():
    UserPhone = request.form.get('UserPhone')
    SecretKey = request.form.get('SecretKey')
    return jsonify(mine(UserPhone,SecretKey))

