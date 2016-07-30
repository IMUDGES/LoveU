# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.xueservice.xue import xueservice


#run模块-------------------------------------------------------------run模块
@app.route('/xue', methods = ['POST', 'GET'])
def xue():
    r = xueservice()
    return jsonify(r.xue())


@app.route('/creatxue', methods = ['POST', 'GET'])
def creatxue():
    r = xueservice()
    return jsonify(r.creat())


@app.route('/getxue', methods=['POST', 'GET'])
def getxue():
    r = xueservice()
    return jsonify(r.get())


@app.route('/canclexue', methods = ['POST', 'GET'])
def canclexue():
    r = xueservice()
    return jsonify(r.cancle())


@app.route('/myxue', methods = ['POST', 'GET'])
def myxue():
    r = xueservice()
    return jsonify(r.myxue())


@app.route('/thisxue', methods = ['GET', 'POST'])
def thisxue():
    r = xueservice()
    return jsonify(r.thisxue())

@app.route('/acceptxue', methods=['GET', 'POST'])
def acceptxue():
    r = xueservice()
    return jsonify(r.accept())

@app.route('/refusexue', methods=['GET', 'POST'])
def refusexue():
    r = xueservice()
    return jsonify(r.refuse())

#run模块结束---------------------------------------------------run模块结束