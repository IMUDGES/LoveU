# -*- coding:utf-8 -*-
from app.db import User, db
from app.bean.rong import ApiClient

class Nickname(object):
    def change(self,userphone,secretkey,newnickname, usersex):
        user = User.query.filter_by(UserPhone=userphone).first()
        if user.SecretKey == secretkey:
            if usersex is not None:
                user.UserSex = int(usersex)
            if newnickname is not None:
                user.NickName = newnickname
            app_key = 'y745wfm8440uv'
            app_secret = '8H4Zs6MenT3Trf'
            api = ApiClient(app_key, app_secret)
            db.session.commit()
            r = api.refreshUser(user['UserId'],user['NickName'],user['UserPhoto'])
            state = 1
            msg = "修改成功！"
            array = {
                'state': state,
                'msg': msg
            }
        else:
            state = 0
            msg = "请先登录！"
            array = {
                'state':state,
                'msg':msg
            }
        return array