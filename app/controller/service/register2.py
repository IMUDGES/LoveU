# -*- coding:utf-8 -*-
from app.db import db, Checkcode

class Register2(object):
    def register2(self, phone, checkcode):
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

