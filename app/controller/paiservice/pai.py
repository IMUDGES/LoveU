# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Money, db
from app.db import Pai
from app.controller.moneyservice.money import moneyservice
from app.controller.service.data import data


class paiservice():

    def pai(self):
        page = int(request.args.get('page'))
        P = Pai.query.filter_by(State=1).paginate(page, 10, False)
        p = P.items
        if p is not None:
            array = {
                'msg': '成功',
                'state': '1',
                'num':len(p)
            }
            list1 = [array]
            d = data()
            for i in range(0, len(p)):
                if p[i] is not None:
                    print(p[i].UserId)
                    a = d.GetOthersData(p[i].UserId)
                    array = {
                        'UserPhoto':a['UserPhoto'],
                        'NickName':a['NickName'],
                        'PaiId': p[i].PaiId,
                        'PaiTitle':p[i].PaiTitle,
                        'UserId': p[i].UserId,
                        'PaiMoney':p[i].PaiMoney,
                        'UpTime':p[i].UpTime,
                        'PaiInformation': p[i].PaiInformation,
                        'PaiImage':p[i].PaiImage,
                        'DownTime':p[i].DownTime
                    }
                    list1.append(array)
            return list1
        else:
            array = {
                'num':0,
                'msg': '信息为空',
                'state': '0'
            }
            list1 = [array]
            list1.append(array)
            return list1

    def get(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        u = User.query.filter_by(UserPhone=UserPhone, SecretKey=SecretKey).first()
        if u is None:
            state = '0'
            msg = '请登录'
        else:
            UserId = u.UserId
            PaiId = int(form.get('PaiId'))
            PaiMoney = int(form.get('PaiMoney'))
            PayPassword = form.get('PayPassword').encode('utf-8')
            p = Pai.query.filter_by(PaiId=PaiId).first()
            if p.State == 0:
                state = '0'
                msg = '拍卖已结束'
            else:
                if p.PaiMoney >= PaiMoney:
                    state = '0'
                    msg = '竞拍价格须高于当前价格'
                else:
                    m = moneyservice()
                    result = m.pay(UserPhone, SecretKey, PayPassword, PaiMoney)
                    if result['state'] == '1':
                        state = '1'
                        msg = '竞拍成功'
                        M = Money.query.filter_by(UserId=p.GetUser).first()
                        M.Money = M.Money+p.PaiMoney
                        p.GetUser = UserId
                        p.PaiMoney = PaiMoney
                    else:
                        state = '0'
                        msg = result['msg']
            array = {
                'state':state,
                'msg':msg
            }
            return array






