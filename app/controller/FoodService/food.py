# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Food, db

class foodservice():
    def food(self):
        page = int(request.args.get('page'))
        #SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        #UserPhone = '2147483647'
        #page = 1
        f = Food.query.paginate(page,10,False)
        p = f.items
        array = {
            'FoodId': p[0].FoodId,
            'UserId': p[0].UserId,
            'FoodArea': p[0].FoodArea,
            'FoodInformation': p[0].FoodInformation,
            'GetUser': p[0].GetUser,
            'FoodTime': p[0].FoodTime,
            'FoodWay': p[0].FoodWay,
            'State': p[0].State
         }
        list1 = [array]
        for i in range(1,len(p)):
            if p[i] is not None:
                array = {
                    'FoodId': p[i].FoodId,
                    'UserId' : p[i].UserId,
                    'FoodArea' : p[i].FoodArea,
                    'FoodInformation' : p[i].FoodInformation,
                    'GetUser' : p[i].GetUser,
                    'FoodTime' : p[i].FoodTime,
                    'FoodWay' : p[i].FoodWay,
                    'State' : p[i].State
                }
                list1.append(array)
        return list1
    def creat(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        #UserPhone = '2147483647'
        #SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                FoodArea = form.get('FoodArea')
                FoodInformation = form.args.get('FoodInformation')
                FoodTime = form.args.get('FoodTime')
                FoodWay = form.args.get('FoodWay')
                #FoodArea = 'hhh'
                #FoodInformation = 'hhh'
                #FoodTime = '2016-07-28 15:31:41'
                #FoodWay = 'hhh'
                UserId = u.UserId
                f =  Food()
                f.UserId = UserId
                f.FoodArea = FoodArea
                f.FoodInformation = FoodInformation
                f.FoodTime = FoodTime
                f.FoodWay = FoodWay
                f.State = 1
                db.session.add(f)
                db.session.commit()
                msg = '1'
            else:
                msg = '0'
        else:
            msg = '0'
        array = {
            'msg' : msg
        }
        return array
    def get(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        FoodId = request.args.get('FoodId')
        #UserPhone = '2147483647'
        #SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        #FoodId = 3
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Food.query.filter_by(FoodId = FoodId).first()
                if f.State == 1:
                    f.GetUser = u.UserId
                    f.State = 0
                    msg = '1'
                else:
                    msg = '约会已结束'
            else:
                msg = '请登录'
        else:
            msg = '请登录'
        array = {
            'msg' : msg
        }
        return array
    def cancle(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        FoodId = request.args.get('FoodId')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Food.query.filter_by(FoodId = FoodId).first()
                db.session.delete(f)
                db.session.commit()
                msg = '1'
            else:
                msg = '请登录'
        else:
         msg = '请登录'
        array = {
            'msg' : msg
        }
        return array
    def myfood(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Food.query.filter(UserId = u.UserId).all()











