# -*- coding:utf-8 -*-
from app.bean.message import Message
from app.db import Checkcode, db


class SendMessage(object):


    def sendmessage(self, phone):
        message = Message()
        checkCode = Checkcode()
        code = message.sendMessage(phone)
        checkCode.CheckCode = code
        checkCode.UserPhone = phone
        db.session.add(checkCode)
        db.session.commit()

