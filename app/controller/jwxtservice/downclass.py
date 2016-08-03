# -*- coding:utf-8 -*-
from app.controller.jwxtservice.jwxtservice import JwxtService
from app.db import db, Class, User


class Downclass(object):
    def downclass(self, userphone, secretkey):
        user = User.query.filter_by(UserPhone=userphone).first()
        if user.SecretKey == secretkey:
            classinfo = Class.query.filter_by(UserId=user.UserId).all()
            print(classinfo)
            msg = "成功！"
            state = 1
            array = {
                'state': state,
                'msg': msg
            }
            return array
        else:
            msg = "请登录！"
            state = 0
            array = {
                'state': state,
                'msg': msg
            }
            return array

downclass = Downclass()
downclass.downclass("11111111114", "61f70c29fda751350de97e7b92163de4")
