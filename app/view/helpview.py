# -*- coding:utf-8 -*-
from flask import jsonify, request
from app import app
from app.controller.helpservice.help import helpservice


#help模块
@app.route('/help', methods = ['GET'])
def help():
    h = helpservice()
    return jsonify(h.help())


@app.route('/creathelp', methods = ['POST', 'GET'])
def creathelp():
    h = helpservice()
    return jsonify(h.creat())


@app.route('/gethelp', methods = ['POST', 'GET'])
def gethelp():
    h = helpservice()
    return jsonify(h.get())


@app.route('/canclehelp', methods = ['POST', 'GET'])
def canclehelp():
    h = helpservice()
    return jsonify(h.cancle())


@app.route('/thishelp', methods = ['POST', 'GET'])
def thishelp():
    h = helpservice()
    return jsonify(h.thishelp())


@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
    h = helpservice()
    return jsonify(h.confirm())


#我发出的未过期的help
@app.route('/myissuehelp_notoverdue', methods = ['POST', 'GET'])
def myissuehelp_notoverdue():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    h = helpservice()
    return jsonify(h.my_issuehelp(1,UserPhone,SecretKey))


#我发出的过期的help
@app.route('/myissuehelp_overdue', methods = ['POST', 'GET'])
def myissuehelp_overdue():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    h = helpservice()
    return jsonify(h.my_issuehelp(0,UserPhone,SecretKey))


#我接受的未过期的help
@app.route('/mygethelp_notoverdue', methods = ['POST', 'GET'])
def mygethelp_notoverdue():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    h = helpservice()
    return jsonify(h.my_gethelp(1,UserPhone,SecretKey))


#我接受的过期的help
@app.route('/mygethelp_overdue', methods = ['POST', 'GET'])
def mygethelp_overdue():
    UserPhone = request.args.get('UserPhone')
    SecretKey = request.args.get('SecretKey')
    h = helpservice()
    return jsonify(h.my_gethelp(0,UserPhone,SecretKey))
#结束