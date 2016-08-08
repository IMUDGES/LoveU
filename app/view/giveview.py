# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.giveservice.give import giveservice



@app.route('/give', methods=['POST', 'GET'])
def give():
    g = giveservice()
    return jsonify(g.give())


@app.route('/creatgive', methods=['POST', 'GET'])
def creatgive():
    g = giveservice()
    return jsonify(g.creat())



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