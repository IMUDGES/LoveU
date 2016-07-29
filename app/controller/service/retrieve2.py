# -*- coding:utf-8 -*-
from app.db import db, Checkcode, User

class Retrieve2(object):
    def Retrieve2(self, phone, checkcode):
        try:
            n = User.query.filter_by(UserPhone=phone).all()
            if len(n) == 0:
                state = 0
                msg = "此手机号还没有被注册!"
                array = {
                    'state': state,
                    'msg': msg
                }
                return array
            m = Checkcode.query.filter_by(UserPhone=phone).all()
            if m[len(m)-1].CheckCode == int(checkcode):
                state = 1
                msg = "成功!"
                array = {
                    'state': state,
                    'msg': msg
                }
                return array
            else:
                state = 0
                msg = "验证码错误!"
                array = {
                    'state': state,
                    'msg': msg
                }
                return array
        except Exception as e:
            print(e)
            state = 0
            msg = "出现奇怪的错误了，一会再试试吧！"
            array = {
                'state': state,
                'msg': msg
            }
            return array
