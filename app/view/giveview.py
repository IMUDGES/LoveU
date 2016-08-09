# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.giveservice.give import giveservice



@app.route('/give', methods=['POST', 'GET'])
def give():
    g = giveservice()
    return jsonify(g.give())


#安卓路由
@app.route('/creatgive', methods=['POST', 'GET'])
def creatgive():
    g = giveservice()
    return jsonify(g.creat())
###


#网站路由
@app.route('/Creatgive', methods=['POST', 'GET'])
def Creatgive():
    g = giveservice()
    return jsonify(g.Creat())
###


@app.route('/givecomment', methods=['POST', 'GET'])
def givecomment():
    g = giveservice()
    return jsonify(g.givecomment())


@app.route('/getgive', methods=['POST', 'GET'])
def getgive():
    g = giveservice()
    return jsonify(g.getgive())


@app.route('/selectgive', methods=['POST','GET'])
def select():
    g = giveservice()
    return jsonify(g.select())


#我发出的未过期的give
@app.route('/myissuegive_notoverdue', methods = ['POST', 'GET'])
def myissuegive_notoverdue():
    g = giveservice()
    return jsonify(g.my_issuegive(1))


#我发出的过期的give
@app.route('/myissuegive_overdue', methods = ['POST', 'GET'])
def myissuegive_overdue():
    g = giveservice()
    return jsonify(g.my_issuegive(0))


#我接受的未过期的give
@app.route('/mygetgive_notoverdue', methods = ['POST', 'GET'])
def mygetgive_notoverdue():
    g = giveservice()
    return jsonify(g.my_getgive(1))


#我接受的过期的give
@app.route('/mygetgive_overdue', methods = ['POST', 'GET'])
def mygetgive_overdue():
    g = giveservice()
    return jsonify(g.my_getgive(0))