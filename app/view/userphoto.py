# -*- coding:utf-8 -*-
from flask import jsonify,request
from app import app
from app.controller.runservice.run import runservice
from app.controller.service.photoservice import Upphoto


@app.route('/userphoto', methods = ['POST', 'GET'])
def userphoto():
    upphoto = Upphoto()
    if request.method == 'POST':
        file = request.files['file']
        if file and upphoto.allowed_file(file.filename):
            #未完成
            pass
    return '1'
