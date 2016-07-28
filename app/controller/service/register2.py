# -*- coding:utf-8 -*-
from app.db import db, Checkcode, User

class Register2(object):
    def register2(self, phone, checkcode):
        try:
            n = User.query.filter_by(UserPhone=phone).all()
            if len(n) != 0:
                msg = 2
                array = {
                    'msg': msg
                }
                return array
            m = Checkcode.query.filter_by(UserPhone=phone).all()
            if m[len(m)-1].CheckCode == int(checkcode):
                msg = 1
                array = {
                    'msg': msg
                }
                return array
            else:
                msg = 0
                array = {
                    'msg': msg
                }
                return array
        except Exception as e:
            print(e)
