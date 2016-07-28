# -*- coding:utf-8 -*-
from app.db import User
from flask import request
from app.db import Food
from flask import jsonify


class foodservice():
    def food(self):
        form = request.form
        SecretKey = form.get('SecretKey')
        UserPhone = form.get('UserPhone')
        page = int(form.get('page'))
        #SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        #UserPhone = '2147483647'
        #page = 1
        if not SecretKey or not UserPhone:
            msg = '请登录'
        else:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if SecretKey == u.SecretKey:
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








