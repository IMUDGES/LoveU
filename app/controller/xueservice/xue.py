# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Xue, db
from app.controller.service.data import data


class xueservice():
    def xue(self):
        page = int(request.args.get('page'))
        # SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        # UserPhone = '2147483647'
        # page = 1
        f = Xue.query.order_by(-Xue.XueId).filter_by(State=1).paginate(page, 10, False)
        p = f.items
        if len(p) > 0:
            array = {
                'msg': '成功',
                'state': '1',
                'num': len(p)
            }
            d = data()
            list1 = []
            for i in range(0, len(p)):
                if p[i] is not None:
                    a = d.GetOthersData(p[i].UserId)
                    array1 = {
                        'UserPhoto': a['UserPhoto'],
                        'NickName': a['NickName'],
                        'UserSex': a['UserSex'],
                        'XueId': p[i].XueId,
                        'UserId': p[i].UserId,
                        'XueArea': p[i].XueArea,
                        'XueInformation': p[i].XueInformation,
                        'GetUser': p[i].GetUser,
                        'XueTime': p[i].XueTime,
                        'State': p[i].State
                    }
                    list1.append(array1)
            array['xuedata'] = list1
            return array
        else:
            array = {
                'num': 0,
                'msg': '信息为空',
                'state': '0'
            }
            return array

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
                p = Xue.query.filter_by(UserId=UserId, State=1).first()
                if p is None:
                    XueArea = form.get('XueArea')
                    XueInformation = form.get('XueInformation')
                    XueTime = form.get('XueTime')
                    # FoodArea = 'hhh'
                    # FoodInformation = 'hhh'
                    # FoodTime = '2016-07-28 15:31:41'
                    # FoodWay = 'hhh'
                    f = Xue()
                    f.UserId = UserId
                    f.XueArea = XueArea
                    f.XueInformation = XueInformation
                    f.XueTime = XueTime
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
        XueId = int(request.args.get('XueId'))
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        # FoodId = 3
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Xue.query.filter_by(XueId=XueId).first()
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
            'msg': msg,
            'state': state
        }
        return array

    def cancle(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        XueId = int(request.args.get('XueId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Xue.query.filter_by(XueId=XueId).first()
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
            'state': state,
            'msg': msg
        }
        return array

    def myrun(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Xue.query.filter_by(UserId=u.UserId).all()
                if p is not None:
                    array = {
                        'msg': '成功',
                        'state': '1'
                    }
                    list1 = []
                    for i in range(0, len(p)):
                        array1 = {
                            'XueId': p[i].XueId,
                            'UserId': p[i].UserId,
                            'XueArea': p[i].XueArea,
                            'XueInformation': p[i].XueInformation,
                            'GetUser': p[i].GetUser,
                            'XueTime': p[i].XueTime,
                            'State': p[i].State
                        }
                        list1.append(array1)
                    array['xuedata'] = list1
                    return array
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
        XueId = int(request.args.get('XueId'))
        p = Xue.query.filter_by(RunId=XueId).first()
        if p is not None:
            array = {
                'msg': '成功',
                'state': '1',
                'XueId': p.XueId,
                'UserId': p.UserId,
                'XueArea': p.XueArea,
                'XueInformation': p.XueInformation,
                'GetUser': p.GetUser,
                'XueTime': p.XueTime,
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
        XueId = int(request.args.get('XueId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Xue.query.filter_by(RunId=XueId).first()
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
        XueId = int(request.args.get('XueId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Xue.query.filter_by(XueId=XueId).first()
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
