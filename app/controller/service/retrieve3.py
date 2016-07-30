# -*- coding:utf-8 -*-
from app.db import db, User
import hashlib


class Retrieve3(object):


    def retrieve3(self, UserPhone, PassWord):
        try:
            nq = User.query.filter_by(UserPhone=UserPhone).all()
            if len(nq) == 0:
                state = 0
                msg = "此手机号还没有被注册！"
                array = {
                    'state': state,
                    'msg': msg
                }
                return array
            m = hashlib.md5()
            m.update(PassWord.encode('utf-8'))
            PassWord = m.hexdigest()
            nq = User.query.filter_by(UserPhone=UserPhone).first()
            nq.PassWord = PassWord
            nq.user.UserPhone = UserPhone
            db.session.commit()
            state = 1
            msg = "成功！"
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
