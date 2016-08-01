# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.moneyservice.money import moneyservice


#钱包模块
@app.route('/sendcheck', methods = ['POST', 'GET'])
def dendcheck():
    m = moneyservice()
    return jsonify(m.sendcheck())


@app.route('/setpsw', methods = ['POST', 'GET'])
def setpsw():
    m = moneyservice()
    return jsonify(m.setpsw())
#end