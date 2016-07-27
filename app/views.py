from flask import jsonify, render_template
from app import app
from controller.Service.login import dologin

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
    print '1'
    return jsonify(dologin())


#@app.route('/creatfood',methods = ['POST', 'GET'])
#def food():










