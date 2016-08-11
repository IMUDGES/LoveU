# -*- coding:utf-8 -*-
from app.controller.service.mineservice import mine
from flask import jsonify
from app import app
from flask import request


@app.route('/myissue')
def MINEDATA():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    a,a1 = mine(UserPhone, SecretKey)
    return jsonify(a)


@app.route('/myget')
def MINEDATA1():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    a, a1 = mine(UserPhone, SecretKey)
    return jsonify(a1)

