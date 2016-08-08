# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.service.refuseservice import Refuseservice


@app.route('/attention', methods = ['POST', 'GET'])
def attention():
    a = Refuseservice()
    return jsonify(a.refuse_other())
