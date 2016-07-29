# -*- coding:utf-8 -*-
from app.db import db, User
import hashlib


class Register3(object):
    user = User()

    def register3(self, UserPhone, PassWord, NickName):
        try:
            nq = User.query.filter_by(UserPhone=UserPhone).all()
            if len(nq) != 0:
                state = 0
                msg = "此手机号已经被注册了亲！"
                array = {
                    'state': state,
                    'msg': msg
                }
                return array
            m = hashlib.md5()
            m.update(PassWord.encode('utf-8'))
            PassWord = m.hexdigest()
            self.user.PassWord = PassWord
            self.user.NickName = NickName
            self.user.UserPhone = UserPhone
            db.session.add(self.user)
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
