# -*- coding:utf-8 -*-
from app.bean.secretkey import Secretkey
from app.db import User
from flask import request
from app.db import Food


class foodservice():
    def creat(self):
        self.Secretkey = request.args.get('SecretKey')
        self.UserPhone = request.args.get()
        if not self.UserPhone or not self.Secretkey:
            msg = '请登录'
        else:
            u = User.query.filter_by(UserPhone = self.UserPhone).first()
            if u.SecretKey != Secretkey:
                msg = '请登录'
            else:
                f = Food
                f.UserId = u.UserId
                f.FoodArea = request.args.get('FoodArea')
                f.FoodInformation = request.args.get('FoodInformation')
                f.FoodTime = request.args.get()






