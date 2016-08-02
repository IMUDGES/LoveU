# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.paiservice.pai import paiservice


@app.route('/pai', methods=['POST', 'GET'])
def pai():
     p = paiservice()
     return jsonify(p.pai())