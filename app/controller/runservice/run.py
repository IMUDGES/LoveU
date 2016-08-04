# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Run, db
from app.controller.service.data import data

class runservice():

    def run(self):
        page = int(request.args.get('page'))
        #SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        #UserPhone = '2147483647'
        #page = 1
        f = Run.query.order_by(-Run.RunId).filter_by(State=1).paginate(page, 10, False)
        p = f.items
        if len(p) > 0:
            array = {
                'num':len(p),
                'msg': '成功',
                'state': '1'
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
                        'RunId': p[i].RunId,
                        'UserId' : p[i].UserId,
                        'RunArea' : p[i].RunArea,
                        'RunInformation' : p[i].RunInformation,
                        'GetUser' : p[i].GetUser,
                        'RunTime' : p[i].RunTime,
                        'State' : p[i].State
                    }
                    list1.append(array1)
            array['rundata'] = list1
            return array
        else:
            array = {
                'num':0,
                'msg': '信息为空',
                'state': '0'
            }
            return array

    def creat(self):
        def creat(self):
            form = request.form
            UserPhone = form.get('UserPhone')
            SecretKey = form.get('SecretKey')
            # UserPhone = '2147483647'
            # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
            if UserPhone and SecretKey:
                u = User.query.filter_by(UserPhone=UserPhone).first()
                if u.SecretKey == SecretKey:
                    UserId = u.UserId
                    p = Run.query.filter_by(UserId=UserId, State=1).first()
                    if p is None:
                        RunArea = form.get('RunArea')
                        RunInformation = form.args.get('RunInformation')
                        RunTime = form.args.get('RunTime')
                        # FoodArea = 'hhh'
                        # FoodInformation = 'hhh'
                        # FoodTime = '2016-07-28 15:31:41'
                        # FoodWay = 'hhh'
                        f = Run()
                        f.UserId = UserId
                        f.RunArea = RunArea
                        f.RunInformation = RunInformation
                        f.RunTime = RunTime
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
                'state': state,
                'msg': msg
            }
            return array

    def get(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        RunId = int(request.args.get('RunId'))
        #UserPhone = '2147483647'
        #SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        #FoodId = 3
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Run.query.filter_by(RunId=RunId).first()
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
        RunId = int(request.args.get('RunId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Run.query.filter_by(FoodId = RunId).first()
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

    def myrun(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Run.query.filter_by(UserId = u.UserId).all()
                if p is not None:
                    array = {
                        'msg' : '成功',
                        'state' : '1'
                    }
                    list1 = [array]
                    for i in range(0,len(p)):
                        array = {
                            'RunId': p[i].RunId,
                            'UserId': p[i].UserId,
                            'RunArea': p[i].RunArea,
                            'RunInformation': p[i].RunInformation,
                            'GetUser': p[i].GetUser,
                            'RunTime': p[i].RunTime,
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

    def thisrun(self):
        RunId = int(request.args.get('RunId'))
        p = Run.query.filter_by(RunId = RunId).first()
        if p is not None:
            array  = {
                'msg' : '成功',
                'state' : '1',
                'RunId': p.RunId,
                'UserId': p.UserId,
                'RunArea': p.RunArea,
                'RunInformation': p.RunInformation,
                'GetUser': p.GetUser,
                'RunTime': p.RunTime,
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
        RunId = int(request.args.get('RunId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Run.query.filter_by(RunId=RunId).first()
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
        RunId = int(request.args.get('RunId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Run.query.filter_by(RunId=RunId).first()
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