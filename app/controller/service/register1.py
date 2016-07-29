# -*- coding:utf-8 -*-
from app.db import db, Checkcode, User
from app.controller.service.sendmessage import SendMessage


class Register1(object):
    def register1(self,UserPhone):
        n = User.query.filter_by(UserPhone=UserPhone).all()
        if len(n) != 0:
            state = 0
            msg = "此手机号已经被注册过了亲!"
            array = {
                'state': state,
                'msg': msg
            }
            return array
        sendMessage = SendMessage()
        sendMessage.sendmessage(UserPhone)
        state = 1
        msg = "成功"
        array = {
            'state':state,
            'msg': msg,
        }
        return array