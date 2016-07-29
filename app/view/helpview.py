# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.helpservice.help import helpservice


@app.route('/help', methods = ['GET'])
def help():
    h = helpservice()
    return jsonify(h.help())