# -*- coding:utf-8 -*-
from app.db import db, User
import hashlib


class Register3(object):
    user = User()

    def register3(self, UserPhone, PassWord, NickName):
        try:
            nq = User.query.filter_by(UserPhone=UserPhone).all()
            if len(nq) != 0:
                msg = 2
                array = {
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
            msg = 1
            array = {
                'msg': msg
            }
            return array
        except Exception as e:
            print(e)
            msg = 0
            array = {
                'msg': msg
            }
            return array
