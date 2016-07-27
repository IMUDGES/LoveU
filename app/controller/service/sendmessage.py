# -*- coding:utf-8 -*-
from app.bean.message import Message
from app.db import Checkcode,db


class SendMessage(object):
    message = Message()
    checkCode = Checkcode()

    def sendmessage(self, phone):
        code = self.message.sendMessage(phone)
        self.checkCode.CheckCode = code
        self.checkCode.UserPhone = phone
        db.session.add(self.checkCode)
        db.session.commit()

