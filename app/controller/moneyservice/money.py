# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Money, db
from app.db import Checkcode
from app.controller.service.sendmessage import SendMessage
from app.bean.md5 import encrypt

class moneyservice():

    def sendcheck(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                s = SendMessage()
                s.sendmessage(UserPhone)
                msg = '成功'
                state = '1'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'
        array = {
            'msg' :msg,
            'state' : state
        }
        return array

    def setpsw(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId
                CheckCode = form.get('CheckCode')
                if CheckCode:
                    c = Checkcode.query.order_by(-Checkcode.CheckId).filter_by(UserPhone = UserPhone, CheckCode = CheckCode).first()
                    if c is not None:
                        m = Money()
                        m.UserId = UserId
                        m.Money = 0
                        m.PayPassword = encrypt(form.get('PayPassword').encode('utf-8'))
                        db.session.add(m)
                        db.session.commit()
                        msg = '设置成功'
                        state = '1'
                    else:
                        msg = '验证码不正确'
                        state = '0'
                else:
                    msg = '验证码不正确'
                    state = '0'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'
        array = {
            'msg' :msg,
            'state' : state
        }
        return array

    def pay(self, UserPhone, SecretKey, PayPassword, MoneyNum):
        userphone = UserPhone
        secretkey = SecretKey
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if userphone and secretkey:
            u = User.query.filter_by(UserPhone=userphone).first()
            if u.SecretKey == secretkey:
                paypassword = encrypt(PayPassword.encode('utf-8'))
                userid = u.UserId
                temp = Money.query.filter_by(UserId=userid).first()
                if temp is None:
                    msg = '请注册钱包'
                    state = '0'
                else:
                    mym = Money.query.filter_by(UserId=userid, PayPassword=paypassword).first()
                    if mym is not None:
                        money = MoneyNum
                        if mym.Money<money:
                            mym.Money = mym.Money - money
                            msg = '支付成功'
                            state = '1'
                        else:
                            msg = '余额不足,请充值'
                            state = '0'
                    else:
                        mym = Money.query.filter_by(UserPhone=UserPhone).first()
                        mym.Num = mym.Num - 1
                        msg = '支付密码错误，今天还有' + mym.Num + '次机会'
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

    def recharge(self, UserPhone, SecretKey, money):
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId
                m = Money.query.filter_by(UserId=UserId).first()
                if m is not None:
                    m.Money = m.Money+money
                    msg = '充值成功'
                    state = '1'
                else:
                    msg = '请完善钱包信息'
                    state = '0'
            else:
                msg = '请登录'
                state = '0'
        else:
            msg = '请登录'
            state = '0'
        array = {
            'msg':msg,
            'state':state
        }
        return array







