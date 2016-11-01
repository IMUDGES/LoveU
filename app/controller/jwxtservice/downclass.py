# -*- coding:utf-8 -*-
from flask import jsonify, request
from app import app
from app.controller.jwxtservice.jwxtservice import JwxtService
from app.db import db, Class, User


class Downclass(object):
    def downclass(self, userphone, secretkey):
        user = User.query.filter_by(UserPhone=userphone).first()
        if user.SecretKey == secretkey:
            classinfo = Class.query.filter_by(UserId=user.UserId).all()
            classinfojson = []
            l = 0
            for i in range(0,8):
                aaa = []
                for j in range(0,12):
                    aaa.append(0)
                classinfojson.append(aaa)

            for q in classinfo:
                classinfojson[q.Day][q.Number] = q.Information
            msg = "成功！"
            state = 1
            array = {
                'state': state,
                'msg': msg,
                'data': classinfojson,
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
