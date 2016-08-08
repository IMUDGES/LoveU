# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.service.attentionservice import Attentionservice


@app.route('/attention', methods = ['POST', 'GET'])
def attention():
    a = Attentionservice()
    return jsonify(a.attention_other())
