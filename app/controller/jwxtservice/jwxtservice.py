# -*- coding:utf-8 -*-
import httplib2
from app.db import db, Class, User, Jwxt
import json


class JwxtService(object):
    def loginService(self, jwxtnumber, jwxtpassword):
        url = "http://183.175.14.250:8080/JwxtInterface/check.html?zjh=" + jwxtnumber + "&mm=" + jwxtpassword
        conn = httplib2.Http()
        resp, content = conn.request(url, "GET")
        print(resp)
        if resp == 1:
            return True
        else:
            return False

    def classService(self, jwxtnumber, jwxtpassword, userid):
        url = "http://183.175.14.250:8080/JwxtInterface/course.html?zjh=" + jwxtnumber + "&mm=" + jwxtpassword
        conn = httplib2.Http()
        resp, content = conn.request(url, "GET")
        array = json.loads(resp)
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
        array = json.loads(resp)
        i = 0
        classes1 = Class()
        classes1.UserId = userid
        db.session.delete(classes1)
        db.session.commit()
        while (i <= 76):
            classes = Class()
            classes.UserId = userid
            classes.Day = int(array[i]['day'])
            classes.Information = array[i]['courseInfo']
            classes.Number = int(array[i]['no'])
            db.session.add(classes)
            db.session.commit()
            i = i + 1

    def inforService(self, jwxtnumber, userid):
        url = "http://183.175.14.250:8080/JwxtInterface/info.html?zjh=" + jwxtnumber
        conn = httplib2.Http()
        resp, content = conn.request(url, "GET")
        user = User.query.filter_by(userid=userid).first()
        array = json.loads(resp)
        user.TrueName = array['name']
        user.UserGrade = array['className']
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


