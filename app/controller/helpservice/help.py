# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Help, db


class helpservice():
    def help(self):
        page = int(request.args.get('page'))
        # SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        # UserPhone = '2147483647'
        # page = 1
        f = Help.query.filter_by(State = 1).paginate(page, 10, False)
        p = f.items
        if len(p) > 0:
            array = {
                'msg': '成功',
                'state': '1',
                'num' : len(p)
            }
            list1 = [array]
            for i in range(0, len(p)):
                if p[i] is not None:
                    array = {
                        'HelpId': p[i].HelpId,
                        'UserId': p[i].UserId,
                        'HelpInformation': p[i].HelpInformation,
                        'HelpMoney' : p[i].HelpMoney,
                        'GetUser': p[i].GetUser,
                        'DownTime': p[i].DownTime,
                        'State': p[i].State
                    }
                    list1.append(array)
            return list1
        else:
            array = {
                'msg': '信息为空',
                'state': '0',
                'num' : 0
            }
            return array

    def creat(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId
                h = Help()
                h.UserId = int(UserId)
                h.HelpMoney = int(form.get('HelpMoney'))
                h.DownTime = form.get('DownTime')
                h.HelpInformation = form.get('HelpInformation').encode('utf-8')
                h.State = 1
                h.Finish = 0
                db.session.add(h)
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
            'state': state,
            'msg': msg
        }
        return array

    def get(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        HelpId = int(request.args.get('HelpId'))
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        # FoodId = 3
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                h = Help.query.filter_by(HelpId=HelpId).first()
                if h.State == 1:
                    h.GetUser = u.UserId
                    h.State = 0
                    msg = '成功'
                    state = '1'
                else:
                    msg = '已结束'
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
        HelpId = int(request.args.get('HelpId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Help.query.filter_by(HelpId=HelpId).first()
                if f.UserId == u.UserId:
                    db.session.delete(f)
                    db.session.commit()
                    msg = '撤销成功'
                    state = '1'
                else:
                    msg = '操作非法'
                    state = '0'
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

    def myfood(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Help.query.filter_by(UserId=u.UserId).all()
                if p is not None:
                    array = {
                        'msg': '成功',
                        'state': '1'
                    }
                    list1 = [array]
                    for i in range(0, len(p)):
                        array = {
                            'HelpId': p[i].HelpId,
                            'UserId': p[i].UserId,
                            'HelpMoney': p[i].HelpMoney,
                            'DownTime': p[i].DownTime,
                            'GetUser': p[i].GetUser,
                            'HelpInformation': p[i].HelpInformation,
                            'Finish': p[i].Finish,
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
        p = Help.query.filter_by(FoodId=FoodId).first()
        if p is not None:
            array = {
                'msg': '成功',
                'state': '1',
                'HelpId': p.HelpId,
                'UserId': p.UserId,
                'HelpMoney': p.HelpMoney,
                'DownTime': p.DownTime,
                'GetUser': p.GetUser,
                'HelpInformation': p.HelpInformation,
                'Finish': p.Finish,
                'State': p.State
            }
        else:
            array = {
                'msg': '没有此ID',
                'state': '0',
            }
        return array

    def confirm(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        FoodId = int(request.args.get('FoodId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Help.query.filter_by(FoodId=FoodId).first()
                if f.UserId == u.UserId:
                    f.Finish = 1
                    msg = '成功'
                    state = '1'
                else:
                    msg = '操作非法'
                    state = '0'
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

