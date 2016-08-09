# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.paiservice.pai import paiservice


@app.route('/pai', methods=['POST', 'GET'])
def pai():
     p = paiservice()
     return jsonify(p.pai())


#安卓路由
@app.route('/creatpai', methods=['POST', 'GET'])
def creatpai():
     p = paiservice()
     return jsonify(p.creat())
###


#网站路由
@app.route('/Creatpai', methods=['POST', 'GET'])
def Creatpai():
     p = paiservice()
     return jsonify(p.Creat())
###


@app.route('/getpai', methods=['POST', 'GET'])
def getpai():
     p = paiservice()
     return jsonify(p.get())


@app.route('/getpaicomment', methods=['POST', 'GET'])
def getpaicomment():
     p = paiservice()
     return jsonify(p.getpaicommment())


@app.route('/sendpaicomment', methods=['POST', 'GET'])
def sendpaiinformation():
     p = paiservice()
     return jsonify(p.sendcomment())


#我发出的未过期的pai
@app.route('/myissuepai_notoverdue', methods = ['POST', 'GET'])
def myissuepai_notoverdue():
    p = paiservice()
    return jsonify(p.my_issuepai(1))


#我发出的过期的pai
@app.route('/myissuepai_overdue', methods = ['POST', 'GET'])
def myissuepai_overdue():
    p = paiservice()
    return jsonify(p.my_issuepai(0))


#我接受的未过期的pai
@app.route('/mygetpai_notoverdue', methods = ['POST', 'GET'])
def mygetpai_notoverdue():
    p = paiservice()
    return jsonify(p.my_getpai(1))


#我接受的过期的pai
@app.route('/mygetpai_overdue', methods = ['POST', 'GET'])
def mygetpai_overdue():
    p = paiservice()
    return jsonify(p.my_getpai(0))