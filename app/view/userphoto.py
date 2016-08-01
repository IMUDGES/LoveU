# -*- coding:utf-8 -*-
from flask import jsonify,request
from app import app
from app.controller.service.photoservice import Upphoto
#未完成


@app.route('/userphoto', methods = ['POST', 'GET'])
def userphoto():
    form = request.form
    UserPhone = form.get('UserPhone')
    SecretKey = form.get('SecretKey')
    file = request.files['photo']
    upphoto = Upphoto()
    return jsonify(upphoto.upuserphoto(file,UserPhone,SecretKey))


