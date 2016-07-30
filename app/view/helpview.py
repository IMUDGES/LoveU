# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.helpservice.help import helpservice


#help模块
@app.route('/help', methods = ['GET'])
def help():
    h = helpservice()
    return jsonify(h.help())


@app.route('/creathelp', methods = ['POST', 'GET'])
def creathelp():
    h = helpservice()
    return jsonify(h.creat())


@app.route('/gethelp', methods = ['POST', 'GET'])
def gethelp():
    h = helpservice()
    return jsonify(h.get())


@app.route('/canclehelp', methods = ['POST', 'GET'])
def canclehelp():
    h = helpservice()
    return jsonify(h.cancle())


@app.route('/thishelp', methods = ['POST', 'GET'])
def thishelp():
    h = helpservice()
    return jsonify(h.thishelp())


@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
    h = helpservice()
    return jsonify(h.confirm())
#结束