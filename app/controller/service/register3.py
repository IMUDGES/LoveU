# -*- coding:utf-8 -*-
from app.db import db, User
import hashlib


class Register3(object):


    def register3(self, UserPhone, PassWord, NickName):
        try:
            user = User()
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
            user.PassWord = PassWord
            user.NickName = NickName
            user.UserPhone = UserPhone
            user.UserPhoto = 'http://7xrqhs.com1.z0.glb.clouddn.com/default1.jpg'
            user.Experience = 0
            user.UserSex = 3
            db.session.add(user)
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
