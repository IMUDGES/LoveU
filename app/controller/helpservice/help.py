# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Help, db
from app.db import Money
from app.controller.service.data import data
from app.controller.moneyservice.money import moneyservice


class helpservice():

    def help(self):
        page = int(request.args.get('page'))
        # SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        # UserPhone = '2147483647'
        # page = 1
        f = Help.query.order_by(-Help.HelpId).filter_by(State = 1).paginate(page, 10, False)
        p = f.items
        if len(p)>0:
            array = {
                'msg': '成功',
                'state': '1',
                'num' : len(p)
            }
            d = data()
            list1 = []
            for i in range(0, len(p)):
                if p[i] is not None:
                    a = d.GetOthersData(p[i].UserId)
                    array1 = {
                        'UserPhoto':a['UserPhoto'],
                        'NickName':a['NickName'],
                        'UserSex':a['UserSex'],
                        'HelpId': p[i].HelpId,
                        'UserId': p[i].UserId,
                        'HelpInformation': p[i].HelpInformation,
                        'HelpMoney' : p[i].HelpMoney,
                        'GetUser': p[i].GetUser,
                        'DownTime': p[i].DownTime,
                        'State': p[i].State
                    }
                    list1.append(array1)
            array['helpdata'] = list1
            return array
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
        PayPassword = form.get('PayPassword')
        HelpMoney = int(form.get('HelpMoney'))
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId
                m = moneyservice()
                result = m.pay(UserPhone, SecretKey, PayPassword, HelpMoney)
                if result['state'] == 1:
                    h = Help()
                    h.UserId = int(UserId)
                    h.HelpMoney = HelpMoney
                    h.DownTime = form.get('DownTime')
                    h.HelpInformation = form.get('HelpInformation')
                    h.State = 1
                    h.Finish = 0
                    db.session.add(h)
                    db.session.commit()
                    state = '1'
                    msg = '创建成功'
                else:
                    state = '0'
                    msg = result['msg']
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
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        HelpId = int(form.get('HelpId'))
        # print(UserPhone)
        # print(SecretKey)
        # print(HelpId)
        # UserPhone = '11111111111'
        # SecretKey = 'b7db48afb289f63d04d8f053824955bb'
        # HelpId = 1
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
        form = request.form
        UserPhone = form.get('UserPhone').encode('utf-8')
        SecretKey = form.get('SecretKey').encode('utf-8')
        HelpId = int(form.get('HelpId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Help.query.filter_by(HelpId=HelpId).first()
                if f.UserId == u.UserId:
                    if f.GetUser is not None:
                        UserId = u.UserId
                        m = Money.query.filter_by(UserId=UserId).first()
                        m.Money = m.Money + f.HelpMoney
                        db.session.delete(f)
                        db.session.commit()
                        msg = '撤销成功'
                        state = '1'
                    else:
                        msg = '已经有人要帮助您了'
                        state = '0'
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

    def my_issuehelp(self, state, User_Phone, Secret_Key):
        UserPhone = User_Phone
        SecretKey = Secret_Key
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Help.query.filter_by(UserId=u.UserId, State=state).all()
                if len(p)>0:
                    array = {
                        'msg': '成功',
                        'state': '1'
                    }
                    list1 = []
                    for i in range(0, len(p)):
                        array1 = {
                            'HelpId': p[i].HelpId,
                            'UserId': p[i].UserId,
                            'HelpMoney': p[i].HelpMoney,
                            'DownTime': p[i].DownTime,
                            'GetUser': p[i].GetUser,
                            'HelpInformation': p[i].HelpInformation,
                            'Finish': p[i].Finish,
                            'State': p[i].State
                        }
                        list1.append(array1)
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

    def my_gethelp(self, state, User_Phone, Secret_Key):
        UserPhone = User_Phone
        SecretKey = Secret_Key
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Help.query.filter_by(GetUser=u.UserId, State=state).all()
                if len(p)>0:
                    array = {
                        'msg': '成功',
                        'state': '1'
                    }
                    list1 = []
                    for i in range(0, len(p)):
                        array1 = {
                            'HelpId': p[i].HelpId,
                            'UserId': p[i].UserId,
                            'HelpMoney': p[i].HelpMoney,
                            'DownTime': p[i].DownTime,
                            'GetUser': p[i].GetUser,
                            'HelpInformation': p[i].HelpInformation,
                            'Finish': p[i].Finish,
                            'State': p[i].State
                        }
                        list1.append(array1)
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

    def thishelp(self):
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
        form = request.form
        UserPhone = form.get('UserPhone').encode('utf-8')
        SecretKey = form.get('SecretKey').encode('utf-8')
        HelpId = int(form.get('HelpId'))
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                f = Help.query.filter_by(HelpId=HelpId).first()
                if f.UserId == u.UserId:
                    m = Money.fiter_by(UserId=f.GetUser).first()
                    m.Money = m.Money + f.HelpMoney
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

