import os
from app.bean.rong import ApiClient
from flask import request
from app.db import db, User


class Imservice(object):
    def gettoken(self,UserPhone):
        try:
            user = User.query.filter_by(UserPhone=UserPhone).first()
            if user.Token != None:
                return user.Token
            app_key = 'y745wfm8440uv'
            app_secret = '8H4Zs6MenT3Trf'
            api = ApiClient(app_key, app_secret)
            r = api.getToken(userId=user.UserId, name=user.NickName,portraitUri=user.UserPhoto)
            r = str(r)
            r = eval(r)
            user.Token = r['token']
            db.session.commit()
            return r['token']
        except Exception as e:
            return "失败"