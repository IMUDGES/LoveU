# -*- coding:utf-8 -*-
import httplib2
from app.db import db, Class, User
import json
from app.controller.jwxtservice.jwxtservice import Jwxt


class upjwxtService(object):
    jwxt = Jwxt()
    def check(self, userphone, secretkey, jwxtnumber, jwxtpassword):
        user = User.query.filter_by(UserPhone=userphone).first()
        print(type(user))
        if user and user['SecretKey'] == secretkey:
            if self.jwxt.loginService(jwxtnumber,jwxtpassword):
                #此步骤没有完成
                pass


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
