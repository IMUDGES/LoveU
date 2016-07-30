# -*- coding:utf-8 -*-
import httplib2
from app.db import db, Class, User, Jwxt
from app.controller.jwxtservice.jwxtservice import JwxtService


class upjwxtService(object):

    def check(self, userphone, secretkey, jwxtnumber, jwxtpassword):
        jwxtservice = JwxtService()
        user = User.query.filter_by(UserPhone=userphone).first()
        print(type(user))
        if user and user['SecretKey'] == secretkey:
            if jwxtservice.loginService(jwxtnumber, jwxtpassword):
                classesid = Class()
                classesidinfo = classesid.query.filter_by(UserId=user['UserId']).first()
                if classesidinfo:
                    jwxtservice.classupdataService(jwxtnumber,jwxtpassword,user['UserId'])
                else:
                    jwxtservice.classService(jwxtnumber, jwxtpassword,user['UserId'])
                jwxtservice.inforService(jwxtnumber, user['UserId'])
                jwxt = Jwxt()
                jwxtinfo = jwxt.query.filter_by(UserId=user['UserId']).first()
                if jwxtinfo:
                    jwxtservice.updatajwxtinfoService(jwxtnumber,jwxtpassword, user['UserId'])
                else:
                    jwxtservice.addjwxtinfoService(jwxtnumber,jwxtpassword, user['UserId'])
                state = 1
                msg = "成功"
                array = {
                    'state': state,
                    'msg': msg
                }
                return array
            else:
                state = 0
                msg = "请使用正确的教务系统账号密码哦！"
                array = {
                    'state':state,
                    'msg': msg
                }
                return array
        else:
            state = 0
            msg = '请记得先登录哦~'
            array = {
                'state': state,
                'msg': msg
            }
            return array
