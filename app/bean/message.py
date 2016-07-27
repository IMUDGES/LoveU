# -*- coding:utf-8 -*-
import httplib
import hashlib
from rand import rand


class Message(object):
    UserName = "yanyongjie"
    PassWord = "15296603340yyjqq"
    m = hashlib.md5()
    m.update(PassWord)
    PassWord = m.hexdigest()
    len = 6
    CheckCode = rand(len)
    content = "【爱大学】，您的验证码为" + CheckCode + "在3分钟内有效"

    def sendMessage(self, phone):
        try:
            url = "/sms?u=" + self.UserName + "&p=" + self.PassWord + "&m=" + phone + "&c=" + self.content
            print url
            conn = httplib.HTTPConnection("www.smsbao.com")
            conn.request("GET", url)
            response = conn.getresponse()
            print response.read()
        except Exception, e:
            print e
        finally:
            if conn:
                conn.close()
            return self.CheckCode


