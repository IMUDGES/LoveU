# -*- coding:utf-8 -*-
import httplib2
from app.db import db, Class, User, Jwxt
from app.controller.jwxtservice.jwxtservice import JwxtService


class upjwxtService(object):
    jwxtservice = JwxtService()
    def check(self, userphone, secretkey, jwxtnumber, jwxtpassword):
        user = User.query.filter_by(UserPhone=userphone).first()
        print(type(user))
        if user and user['SecretKey'] == secretkey:
            if self.jwxtservice.loginService(jwxtnumber, jwxtpassword):
                classesid = Class()
                classesidinfo = classesid.query.filter_by(UserId=user['UserId']).first()
                if classesidinfo:
                    self.jwxtservice.classupdataService(jwxtnumber,jwxtpassword,user['UserId'])
                else:
                    self.jwxtservice.classService(jwxtnumber, jwxtpassword,user['UserId'])
                self.jwxtservice.inforService(jwxtnumber, user['UserId'])
                jwxt = Jwxt()
                jwxtinfo = jwxt.query.filter_by(UserId=user['UserId']).first()
                if jwxtinfo:
                    self.jwxtservice.updatajwxtinfoService(jwxtnumber,jwxtpassword, user['UserId'])
                else:
                    self.jwxtservice.addjwxtinfoService(jwxtnumber,jwxtpassword, user['UserId'])
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
        else:
            msg = 0
            array = {
                'msg': msg
            }
            return array
