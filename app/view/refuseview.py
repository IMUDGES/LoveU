# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.service.refuseservice import Refuseservice


@app.route('/refuse', methods = ['POST', 'GET'])
def refuse():
    a = Refuseservice()
    return jsonify(a.refuse_other())
