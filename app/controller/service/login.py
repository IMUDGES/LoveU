# -*- coding:utf-8 -*-
from app.bean.secretkey import Secretkey
from app.db import User
from flask import request
import hashlib


def dologin():
    form = request.form
    UserPhone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    u = User.query.filter_by(UserPhone=UserPhone).first()
    if u is None:
        msg = '0'
        SecretKey = None
    else:
        m = PassWord
        password = hashlib.md5()
        password.update(m)
        psw = password.hexdigest()
        if psw == u.PassWord:
            msg = '1'
            S = Secretkey()
            SecretKey = S.GetSecretKey()
            u.SecretKey = SecretKey
        else:
            msg = '0'
            SecretKey = None
    array = {
        'msg': msg,
        'SecretKey': SecretKey
    }
    return array