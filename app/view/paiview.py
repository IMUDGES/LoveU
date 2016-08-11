# -*- coding:utf-8 -*-
from flask import jsonify, request
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


@app.route('/pai_detail', methods=['POST', 'GET'])
def pai_detail():
     p = paiservice()
     return jsonify(p.thispai())


#我发出的未过期的pai
@app.route('/myissuepai_notoverdue', methods = ['POST', 'GET'])
def myissuepai_notoverdue():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    p = paiservice()
    return jsonify(p.my_issuepai(1,UserPhone,SecretKey))


#我发出的过期的pai
@app.route('/myissuepai_overdue', methods = ['POST', 'GET'])
def myissuepai_overdue():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    p = paiservice()
    return jsonify(p.my_issuepai(0,UserPhone,SecretKey))


#我接受的未过期的pai
@app.route('/mygetpai_notoverdue', methods = ['POST', 'GET'])
def mygetpai_notoverdue():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    p = paiservice()
    return jsonify(p.my_getpai(1,UserPhone,SecretKey))


#我接受的过期的pai
@app.route('/mygetpai_overdue', methods = ['POST', 'GET'])
def mygetpai_overdue():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    p = paiservice()
    return jsonify(p.my_getpai(0,UserPhone,SecretKey))