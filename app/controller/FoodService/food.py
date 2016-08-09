# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Food, db
from app.controller.service.data import data

class foodservice():

    def food(self):
        page = int(request.args.get('page'))
        #SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        #UserPhone = '2147483647'
        #page = 1
        f = Food.query.order_by(-Food.FoodId).filter_by(State=1).paginate(page,10,False)
        p = f.items
        if len(p)>0:
            array = {
                'msg': '成功',
                'state': '1',
                'num':len(p)
            }
            d = data()
            list1 = []
            for i in range(0,len(p)):
                if p[i] is not None:
                    a = d.GetOthersData(p[i].UserId)
                    array1 = {
                        'UserPhoto':a['UserPhoto'],
                        'NickName':a['NickName'],
                        'UserSex':a['UserSex'],
                        'FoodId': p[i].FoodId,
                        'UserId' : p[i].UserId,
                        'FoodArea' : p[i].FoodArea,
                        'FoodInformation' : p[i].FoodInformation,
                        'GetUser' : p[i].GetUser,
                        'FoodTime' : p[i].FoodTime,
                        'FoodWay' : p[i].FoodWay,
                        'State' : p[i].State
                    }
                    list1.append(array1)
            array['fooddata'] = list1
            return array
        else:
            array = {
                'num':0,
                'msg': '信息为空',
                'state': '0'
            }
            return array

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
                myf = Food.query.filter_by(UserId = UserId, State = 1).first()
                if myf is not None:
                    msg = '已有约会'
                    state = '0'
                else:
                    FoodArea = form.get('FoodArea')
                    FoodInformation = form.get('FoodInformation')
                    FoodTime = form.get('FoodTime')
                    FoodWay = form.get('FoodWay')
                    #FoodArea = lll'hhh'
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
                msg = '请登录'
        else:
            state = '0'
            msg = '请登录'
        array = {
            'state' : state,
            'msg' : msg
        }
        return array

    def get(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        FoodId = int(form.get('FoodId'))
        #UserPhone = '2147483647'
        #SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        #FoodId = 3
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Food.query.filter_by(FoodId = FoodId).first()
                if f.State == 1:
                    f.GetUser = u.UserId
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
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        FoodId = int(form.get('FoodId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Food.query.filter_by(FoodId = FoodId).first()
                if f.UserId == u.UserId:
                    if f.State == 1:
                        db.session.delete(f)
                        db.session.commit()
                        msg = '撤销成功'
                        state = '1'
                    else:
                        msg = '当前不能撤销'
                        state = '0'
                else:
                    msg = '非法操作'
                    state = '0'
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

    def my_issuefood(self,state):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Food.query.filter_by(UserId=u.UserId, State=state).all()
                if len(p)>0:
                    array = {
                        'msg' : '成功',
                        'state' : '1'
                    }
                    list1 = []
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
                    array['data'] = list1
                else:
                    array = {
                        'msg': '没有信息',
                        'state': '0'
                    }
            else:
                array = {
                    'msg': '请登录',
                    'state': '0'
                }
        else:
            array = {
                'msg': '请登录',
                'state': '0'
            }
        return array

    def my_getfood(self, state):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Food.query.filter_by(GetUser=u.UserId, State=state).all()
                if len(p)>0:
                    array = {
                        'msg': '成功',
                        'state': '1'
                    }
                    list1 = []
                    for i in range(0, len(p)):
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
                    array['data'] = list1
                else:
                    array = {
                        'msg': '没有信息',
                        'state': '0'
                    }
            else:
                array = {
                    'msg': '请登录',
                    'state': '0'
                }
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













