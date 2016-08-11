# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.imservice.im import Imservice



@app.route('/getfriends', methods = ['GET','POST'])
def getfriends():
    i = Imservice()
    return jsonify(i.getfriends())