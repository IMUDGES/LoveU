# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.paiservice.pai import paiservice


@app.route('/pai', methods=['POST', 'GET'])
def pai():
     p = paiservice()
     return jsonify(p.pai())


@app.route('/creatpai', methods=['POST', 'GET'])
def creatpai():
     p = paiservice()
     return jsonify(p.creat())


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