# -*- coding:utf-8 -*-
from app.bean.secretkey import Secretkey
from app.db import User
from flask import request
import hashlib
from app.bean.rong import ApiClient
from app.controller.imservice.im import Imservice


def dologin():
    form = request.form
    UserPhone = form.get('UserPhone')
    PassWord = form.get('PassWord')
    u = User.query.filter_by(UserPhone=UserPhone).first()
    print (UserPhone)
    token = None
    if u is None:
        msg = '用户不存在'
        state = '0'
        SecretKey = None
        UserPhoto = None
    else:
        m = PassWord.encode('utf-8')
        password = hashlib.md5()
        password.update(m)
        psw = password.hexdigest()
        print (psw)
        print (u.PassWord)
        if psw == u.PassWord:
            i = Imservice()
            token = i.gettoken(UserPhone)
            state = '1'
            msg = '登陆成功'
            S = Secretkey()
            SecretKey = S.GetSecretKey()
            u.SecretKey = SecretKey
            UserPhoto = u.UserPhoto
        else:
            msg = '账号或密码错误'
            state = '0'
            SecretKey = None
            UserPhoto = None
    array = {
        'msg': msg,
        'state' : state,
        'SecretKey': SecretKey,
        'token':token,
        'UserPhoto':UserPhoto
    }
    return array