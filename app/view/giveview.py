# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.giveservice.give import giveservice



@app.route('/give', methods=['POST', 'GET'])
def give():
    g = giveservice()
    return jsonify(g.give())



@app.route('/givecomment', methods=['POST', 'GET'])
def givecomment():
    g = giveservice()
    return jsonify(g.givecomment())


@app.route('/getgive', methods=['POST', 'GET'])
def getgive():
    g = giveservice()
    return jsonify(g.getgive())