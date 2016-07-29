# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Food, db

class foodservice():
    def food(self):
        page = int(request.args.get('page'))
        #SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        #UserPhone = '2147483647'
        #page = 1
        f = Food.query.filter_by(State = 1).paginate(page, 10, False)
        p = f.items
        if len(p) > 0:
            array = {
                'msg': '成功',
                'state': '1',
                'num' : len(p)
            }
            list1 = [array]
            for i in range(0,len(p)):
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
        else:
            array = {
                'msg': '信息为空',
                'state': '0',
                'num' : 0
            }
    def creat(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        #UserPhone = '2147483647'
        #SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId
                p = Food.query.filter_by(UserId = UserId, State = 1).first()
                if p is None:
                    FoodArea = form.get('FoodArea')
                    FoodInformation = form.args.get('FoodInformation')
                    FoodTime = form.args.get('FoodTime')
                    FoodWay = form.args.get('FoodWay')
                    #FoodArea = 'hhh'
                    #FoodInformation = 'hhh'
                    #FoodTime = '2016-07-28 15:31:41'
                    #FoodWay = 'hhh'
                    f =  Food()
                    f.UserId = UserId
                    f.FoodArea = FoodArea
                    f.FoodInformation = FoodInformation
                    f.FoodTime = FoodTime
                    f.FoodWay = FoodWay
                    f.State = 1
                    db.session.add(f)
                    db.session.commit()
                    state = '1'
                    msg = '创建成功'
                else:
                    state = '0'
                    msg = '已有约会，创建失败'
            else:
                state = '0'
                msg = '创建失败'
        else:
            state = '0'
            msg = '创建失败'
        array = {
            'state' : state,
            'msg' : msg
        }
        return array
    def get(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        FoodId = int(request.args.get('FoodId'))
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
                    msg = '成功'
                    state = '1'
                else:
                    msg = '约会已结束'
                    state = '0'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'
        array = {
            'msg' : msg,
            'state' : state
        }
        return array
    def cancle(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        FoodId = int(request.args.get('FoodId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Food.query.filter_by(FoodId = FoodId).first()
                db.session.delete(f)
                db.session.commit()
                msg = '撤销成功'
                state = '1'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'
        array = {
            'state' : state,
            'msg' : msg
        }
        return array
    def myfood(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Food.query.filter_by(UserId = u.UserId).all()
                if p is not None:
                    array = {
                        'msg' : '成功',
                        'state' : '1'
                    }
                    list1 = [array]
                    for i in range(0,len(p)):
                        array = {
                            'FoodId': p[i].FoodId,
                            'UserId': p[i].UserId,
                            'FoodArea': p[i].FoodArea,
                            'FoodInformation': p[i].FoodInformation,
                            'GetUser': p[i].GetUser,
                            'FoodTime': p[i].FoodTime,
                            'FoodWay': p[i].FoodWay,
                            'State': p[i].State
                        }
                        list1.append(array)
                    return list1
            else:
                array = {
                    'msg': '请登录',
                    'state': '0'
                }
                return array
        else:
            array = {
                'msg': '请登录',
                'state': '0'
            }
            return array
    def thisfood(self):
        FoodId = int(request.args.get('FoodId'))
        p = Food.query.filter_by(FoodId = FoodId).first()
        if p is not None:
            array  = {
                'msg' : '成功',
                'state' : '1',
                'FoodId': p.FoodId,
                'UserId': p.UserId,
                'FoodArea': p.FoodArea,
                'FoodInformation': p.FoodInformation,
                'GetUser': p.GetUser,
                'FoodTime': p.FoodTime,
                'FoodWay': p.FoodWay,
                'State': p.State
            }
        else:
            array = {
                'msg': '失败',
                'state': '0',
            }
        return array
    def accept(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        FoodId = int(request.args.get('FoodId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Food.query.filter_by(FoodId=FoodId).first()
                f.State = 1
                msg = '成功'
                state = '1'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'
        array = {
            'state': state,
            'msg': msg
        }
        return array
    def refuse(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        FoodId = int(request.args.get('FoodId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Food.query.filter_by(FoodId=FoodId).first()
                f.GetUser = None
                msg = '已拒绝'
                state = '1'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'
        array = {
            'state': state,
            'msg': msg
        }
        return array













