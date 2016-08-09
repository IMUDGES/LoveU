# -*- coding:utf-8 -*-
from app.db import User, db

class Nickname(object):
    def change(self,userphone,secretkey,newnickname, usersex):
        user = User.query.filler_by(userphone=userphone).first()
        if user.SecretKey == secretkey:
            if usersex is not None:
                user.UserSex = usersex
            if newnickname is not None:
                user.NickName = newnickname
            db.session.commit()
            state = 1
            msg = "昵称修改成功！"
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