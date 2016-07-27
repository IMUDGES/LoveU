# -*- coding:utf-8 -*-
from flask import jsonify
from flask import request, render_template
from app import app
from app.controller.service.sendmessage import SendMessage
from app.controller.service.login import dologin


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
    return jsonify(dologin())


@app.route('/register1', methods=['POST'])
def register1():
    form = request.form
    UserPhone = form.get('UserPhone').encode('utf-8')
    print (UserPhone)
    sendMessage = SendMessage()
    sendMessage.sendmessage(UserPhone)
    msg = 1
    array = {
        'msg': msg,
    }
    return jsonify(array)

