# -*- coding:utf-8 -*-
from flask import jsonify,request
from app import app
from app.controller.service.photoservice import Upphoto


#安卓头像修改
@app.route('/userphoto', methods = ['POST', 'GET'])
def userphoto():
    form = request.form
    UserPhone = form.get('UserPhone')
    SecretKey = form.get('SecretKey')
    file = request.files['photo']
    upphoto = Upphoto()
    return jsonify(upphoto.upuserphoto(file,UserPhone,SecretKey))
###


#网站头像修改
@app.route('/Userphoto', methods = ['POST', 'GET'])
def Userphoto():
    form = request.form
    UserPhone = form.get('UserPhone')
    SecretKey = form.get('SecretKey')
    file = request.files.getlist('file')
    upphoto = Upphoto()
    return jsonify(upphoto.upuserphoto(file,UserPhone,SecretKey))
###

