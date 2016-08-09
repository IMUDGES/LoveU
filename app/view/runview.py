# -*- coding:utf-8 -*-
from flask import jsonify
from app import app
from app.controller.runservice.run import runservice


#run模块-------------------------------------------------------------run模块
@app.route('/run', methods = ['POST', 'GET'])
def run():
    r = runservice()
    return jsonify(r.run())


@app.route('/creatrun', methods = ['POST', 'GET'])
def creatrun():
    r = runservice()
    return jsonify(r.creat())


@app.route('/getrun', methods=['POST', 'GET'])
def getrun():
    r = runservice()
    return jsonify(r.get())


@app.route('/canclerun', methods = ['POST', 'GET'])
def canclerun():
    r = runservice()
    return jsonify(r.cancle())


@app.route('/thisrun', methods = ['GET', 'POST'])
def thisrun():
    r = runservice()
    return jsonify(r.thisrun())


@app.route('/acceptrun', methods=['GET', 'POST'])
def acceptrun():
    r = runservice()
    return jsonify(r.accept())


@app.route('/refuserun', methods=['GET', 'POST'])
def refuserun():
    r = runservice()
    return jsonify(r.refuse())


#我发出的未过期的give
@app.route('/myissuerun_notoverdue', methods = ['POST', 'GET'])
def myissuerun_notoverdue():
    r = runservice()
    return jsonify(r.my_issuerun(1))


#我发出的过期的food
@app.route('/myissuerun_overdue', methods = ['POST', 'GET'])
def myissuerun_overdue():
    r = runservice()
    return jsonify(r.my_issuerun(0))


#我接受的未过期的food
@app.route('/mygetrun_notoverdue', methods = ['POST', 'GET'])
def mygetrun_notoverdue():
    r = runservice()
    return jsonify(r.my_getrun(1))


#我接受的过期的food
@app.route('/mygetrun_overdue', methods = ['POST', 'GET'])
def mygetrun_overdue():
    r = runservice()
    return jsonify(r.my_getrun(0))
#run模块结束---------------------------------------------------run模块结束