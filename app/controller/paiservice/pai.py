# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Money, db
from app.db import Pai, Paicomment
from app.controller.moneyservice.money import moneyservice
from app.controller.service.data import data


class paiservice():

    def pai(self):
        page = int(request.args.get('page'))
        P = Pai.query.filter_by(State=1).paginate(page, 10, False)
        p = P.items
        if len(p)>0:
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
                        'UserSex':a['UserSex'],
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
            PayPassword = form.get('PayPassword')
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

    def getpaicommment(self):
        PaiId = int(request.args.get('PaiId'))
        pc = Paicomment.query.filter_by(PaiId=PaiId).all()
        if len(pc)>0:
            array = {
                'msg': '成功',
                'state': '1',
                'num': len(pc)
            }
            list1 = [array]
            d = data()
            for i in range(0, len(pc)):
                if len(pc)>0:
                    a = d.GetOthersData(pc[i].UserId)
                    array = {
                        'UserPhoto': a['UserPhoto'],
                        'NickName': a['NickName'],
                        'UserSex':a['UserSex'],
                        'CommentId':pc[i].CommentId,
                        'CommentInformation':pc[i].CommentInformation,
                        'PaiId':pc[i].PaiId
                    }
                    list1.append(array)
            return list1
        else:
            array = {
                'msg': '失败',
                'state': '0',
                'num': 0
            }
            list1 = [array]
            list1.append(array)
            return list1

    def sendcomment(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        PaiId =  form.get('PaiId')
        CommentInformation = form.get('CommentInformation')
        u = User.query.filter_by(UserPhone=UserPhone, SecretKey=SecretKey).first()
        if u.UserId is None:
            state = '0'
            msg = '请登录'
        else:
            if CommentInformation is None:
                state = '0'
                msg = '评论内容不能为空'
            else:
                state = '1'
                msg = '评论成功'
                p = Paicomment()
                p.CommentInformation = CommentInformation
                p.PaiId = PaiId
                p.UserId = u.UserId
                db.session.add(p)
                db.session.commit()
        array = {
            'state':state,
            'msg':msg
        }
        return array










