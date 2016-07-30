# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Money, db
from app.db import Checkcode
from app.controller.service.sendmessage import SendMessage
from app.bean.md5 import encrypt

class money():
    def sendcheck(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                s = SendMessage()
                s.sendmessage(UserPhone)
                msg = '成功'
                state = '1'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'
        array = {
            'msg' :msg,
            'state' : state
        }
        return array
    def setpsw(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId
                CheckCode = form.get('CheckCode')
                if CheckCode:
                    c = Checkcode.query.filter_by(UserPhone = UserPhone, CheckCode = CheckCode).first()
                    if c is not None:
                        m = Money()
                        m.UserId = UserId
                        m.Money = 0
                        m.PayPassword = encrypt(form.get('PayPassword').encode('utf-8'))
                        db.session.add(m)
                        db.session.commit()
                        msg = '设置成功'
                        state = '1'
                    else:
                        msg = '验证码不正确'
                        state = '0'
                else:
                    msg = '验证码不正确'
                    state = '0'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'




