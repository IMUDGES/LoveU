import os
from app.bean.rong import ApiClient
from flask import request
from app.db import db, User


class Imservice(object):
    def gettoken(self):
        try:
            UserPhone = request.args.get('UserPhone')
            SecretKey = request.args.get('SecretKey')
            user = User.query.filter_by(UserPhone=UserPhone).first()
            if SecretKey != user['SecretKey']:
                array = {
                    'msg': '请登陆后在尝试',
                    'state': '0',
                }
                return array
            if user['Token'] != None:
                array = {
                    'msg': '成功',
                    'state': '1',
                    'token': user['Token']
                }
                return array
            app_key = 'y745wfm8440uv'
            app_secret = '8H4Zs6MenT3Trf'
            api = ApiClient(app_key, app_secret)
            r = api.getToken(userId=user['UserId'], name=user['NickName'],portraitUri=user['UserPhoto'])
            array = {
                'msg': '成功',
                'state': '1',
                'token': user['Token']
            }
            return array
        except Exception as e:
            array = {
                'msg': '失败',
                'state': '0',
            }
            return array