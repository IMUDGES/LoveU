# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.foodservice.food import foodservice


#food模块
@app.route('/food', methods = ['POST', 'GET'])
def food():
    f = foodservice()
    return jsonify(f.food())


@app.route('/creatfood', methods = ['POST', 'GET'])
def creatfood():
    f = foodservice()
    return jsonify(f.creat())


@app.route('/getfood', methods=['POST', 'GET'])
def getfood():
    f = foodservice()
    return jsonify(f.get())


@app.route('/canclefood', methods = ['POST', 'GET'])
def canclefood():
    f = foodservice()
    return jsonify(f.cancle())


#我发出的未过期的food
@app.route('/myissuefood_notoverdue', methods = ['POST', 'GET'])
def myissuefood_notoverdue():
    f = foodservice()
    return jsonify(f.my_issuefood(1))


#我发出的过期的food
@app.route('/myissuefood_overdue', methods = ['POST', 'GET'])
def myissuefood_overdue():
    f = foodservice()
    return jsonify(f.my_issuefood(0))


#我接受的未过期的food
@app.route('/mygetfood_notoverdue', methods = ['POST', 'GET'])
def mygetfood_notoverdue():
    f = foodservice()
    return jsonify(f.my_getfood(1))


#我接受的过期的food
@app.route('/mygetfood_overdue', methods = ['POST', 'GET'])
def mygetfood_overdue():
    f = foodservice()
    return jsonify(f.my_getfood(0))


@app.route('/thisfood', methods = ['GET', 'POST'])
def thisfood():
    f= foodservice()
    return jsonify(f.thisfood())
#food模块结束