# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.moneyservice.money import moneyservice
from flask import request


#钱包模块
@app.route('/sendcheck', methods = ['POST', 'GET'])
def dendcheck():
    m = moneyservice()
    return jsonify(m.sendcheck())


@app.route('/setpsw', methods = ['POST', 'GET'])
def setpsw():
    m = moneyservice()
    return jsonify(m.setpsw())

@app.route('/recharge', methods=['POST', 'GET'])
def srecharge():
    form = request.form
    UserPhone = form.get('UserPhone')
    SecretKey = form.get('SecretKey')
    Money = int(form.get('Money'))
    m = moneyservice()
    return jsonify(m.recharge(UserPhone,SecretKey,Money))
#end