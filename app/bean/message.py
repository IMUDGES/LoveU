# -*- coding:utf-8 -*-
import httplib2
import hashlib
from app.bean.rand import rand


class Message(object):
    UserName = "yanyongjie".encode('utf-8')
    PassWord = "15296603340yyjqq".encode('utf-8')
    m = hashlib.md5()
    m.update(PassWord)
    PassWord = m.hexdigest()
    len = 6
    CheckCode = rand(len)
    content = "【爱大学】，您的验证码为" + CheckCode + "在3分钟内有效"
    def sendMessage(self, phone):
        try:
            url = "www.smsbao.com/sms?u=" + self.UserName.decode('utf-8') + "&p=" + self.PassWord.decode('utf-8') + \
                  "&m=" + phone + "&c=" + self.content.decode('utf-8')
            print(url)
            conn = httplib2.Http('.cache')
            resp, content = conn.request(url, "GET")
        except Exception as e:
            print(e)
        finally:
            return self.CheckCode



