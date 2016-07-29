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


@app.route('/myfood', methods = ['POST', 'GET'])
def myfood():
    f = foodservice()
    return jsonify(f.myfood())


@app.route('/thisfood', methods = ['GET', 'POST'])
def thisfood():
    f= foodservice()
    return jsonify(f.thisfood())
#food模块结束