# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.imservice.im import Imservice

@app.route('/gettoken', methods = ['GET'])
def help():
    i = Imservice()
    return jsonify(i.gettoken())