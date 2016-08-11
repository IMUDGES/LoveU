# -*- coding:utf-8 -*-
import httplib2
from app.db import db, Class, User, Jwxt
import json


class JwxtService(object):
    # 教务系统账号，教务系统密码，课程号，课序号
    def chooseClass(self, JwxtNumber, JwxtPassword, ClassNumber, ClassOrder):
        if ClassOrder < 10:
            ClassOrder = '0' + str(ClassOrder)
        else:
            ClassOrder = str(ClassOrder)
        h = httplib2.Http()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
            "Host": "jwxt.imu.edu.cn",
            "Referer": "http://jwxt.imu.edu.cn/logout.do",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
        resp, content = h.request("http://jwxt.imu.edu.cn/loginAction.do?zjh=" + JwxtNumber + "&mm=" + JwxtPassword,
                                  "GET", headers=headers)
        print(resp)
        cookie = resp['set-cookie'].replace('; path=/', "")
        headers['Cookie'] = cookie
        resp2, content2 = h.request("http://jwxt.imu.edu.cn/xkAction.do?actionType=6", "GET", headers=headers)
        resp3, content3 = h.request("http://jwxt.imu.edu.cn/xkAction.do?actionType=-1&fajhh=32874", "GET",
                                    headers=headers)
        resp4, content4 = h.request("http://jwxt.imu.edu.cn/xkAction.do?actionType=2&pageNumber=-1&oper1=ori", "GET",
                                    headers=headers)
        resp5, content5 = h.request(
            "http://jwxt.imu.edu.cn/xkAction.do?jhxn=&kcsxdm=&kch=" + ClassNumber + "&cxkxh=&actionType=2&oper2=gl&pageNumber=-1",
            "GET", headers=headers)
        resp6, content6 = h.request(
            "http://jwxt.imu.edu.cn/xkAction.do?kcId=" + ClassNumber + "_" + ClassOrder + "&preActionType=2&actionType=9",
            "GET", headers=headers)
        print(content6.decode('gb2312'))
        # print(resp)

    def loginService(self, jwxtnumber, jwxtpassword):
        url = "http://183.175.14.250:8080/JwxtInterface/check.html?zjh=" + jwxtnumber + "&mm=" + jwxtpassword
        conn = httplib2.Http()
        resp, content = conn.request(url, "GET")
        if int(content) == 1:
            return True
        else:
            return False

    def classService(self, jwxtnumber, jwxtpassword, userid):
        url = "http://183.175.14.250:8080/JwxtInterface/course.html?zjh=" + jwxtnumber + "&mm=" + jwxtpassword
        conn = httplib2.Http()
        resp, content = conn.request(url, "GET")
        array = content.decode('gbk')
        array = eval(str(array))
        print(array)
        i = 0
        while(i<=76):
            classes = Class()
            classes.UserId = userid
            classes.Day = int(array[i]['day'])
            classes.Information = array[i]['courseInfo']
            classes.Number = int(array[i]['no'])
            db.session.add(classes)
            db.session.commit()
            i = i + 1

    def classupdataService(self, jwxtnumber, jwxtpassword, userid):
        url = "http://183.175.14.250:8080/JwxtInterface/course.html?zjh=" + jwxtnumber + "&mm=" + jwxtpassword
        conn = httplib2.Http()
        resp, content = conn.request(url, "GET")
        array = content.decode('gbk')
        array = eval(str(array))
        print(array)
        q = 0
        classes1 = Class.query.filter_by(UserId=userid).all()
        for i in range(0, len(classes1)):
            db.session.delete(classes1[i])
            db.session.commit()
        while (q <= 76):
            classes = Class()
            classes.UserId = userid
            classes.Day = int(array[q]['day'])
            classes.Information = array[q]['courseInfo']
            classes.Number = int(array[q]['no'])
            db.session.add(classes)
            db.session.commit()
            q = q + 1

    def inforService(self, jwxtnumber, userid):
        url = "http://183.175.14.250:8080/JwxtInterface/info.html?zjh=" + jwxtnumber
        conn = httplib2.Http()
        resp, content = conn.request(url, "GET")
        user = User.query.filter_by(UserId=userid).first()
        array = content.decode('gbk')
        array = eval(str(array))
        user.TrueName = array['name']
        user.UserGrade = array['className'][4]+array['className'][5]+array['className'][6]
        user.UserMajor = array['profession']
        if array['sex'] == '男':
            User.UserSex = 1
        else:
            User.UserSex = 0
        db.session.commit()

    def addjwxtinfoService(self, jwxtnumber, jwxtpassword, userid):
        jwxt = Jwxt()
        jwxt.UserId = userid
        jwxt.JwxtNumber = jwxtnumber
        jwxt.JwxtPassword = jwxtpassword
        db.session.add(jwxt)
        db.session.commit()

    def updatajwxtinfoService(self, jwxtnumber, jwxtpassword, userid):
        u = Jwxt.query.filter_by(UserId=userid).first()
        u.JwxtNumber = jwxtnumber
        u.JwxtPassword = jwxtpassword
        db.session.commit()


