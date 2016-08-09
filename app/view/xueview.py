# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.xueservice.xue import xueservice


#xue模块-------------------------------------------------------------xue模块
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


#我发出的未过期的give
@app.route('/myissuexue_notoverdue', methods = ['POST', 'GET'])
def myissuexue_notoverdue():
    x = xueservice()
    return jsonify(x.my_issuexue(1))


#我发出的过期的food
@app.route('/myissuexue_overdue', methods = ['POST', 'GET'])
def myissuexue_overdue():
    x = xueservice()
    return jsonify(x.my_issuexue(0))


#我接受的未过期的food
@app.route('/mygetxue_notoverdue', methods = ['POST', 'GET'])
def mygetxue_notoverdue():
    x = xueservice()
    return jsonify(x.my_getxue(1))


#我接受的过期的food
@app.route('/mygetxue_overdue', methods = ['POST', 'GET'])
def mygetxue_overdue():
    x = xueservice()
    return jsonify(x.my_getxue(0))
#xue模块结束---------------------------------------------------xue模块结束