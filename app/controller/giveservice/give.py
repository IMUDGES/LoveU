# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Give, db, Givecomment
from app.controller.service.data import data
from app.bean.qiniuup import Qiniuup



class giveservice():

    def give(self):
        page = int(request.args.get('page'))
        # SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        # UserPhone = '2147483647'
        # page = 1
        f = Give.query.order_by(-Give.GiveId).filter_by(State=1).paginate(page, 10, False)
        p = f.items
        if len(p)>0:
            array = {
                'msg': '成功',
                'state': '1',
                'num':len(p)
            }
            d = data()
            list1 = [array]
            for i in range(0, len(p)):
                if p[i] is not None:
                    a = d.GetOthersData(p[i].UserId)
                    array = {
                        'UserPhoto':a['UserPhoto'],
                        'UserSex':a['UserSex'],
                        'NickName':a['NickName'],
                        'GiveId': p[i].GiveId,
                        'UserId': p[i].UserId,
                        'GiveInformation': p[i].GiveInformation,
                        'GiveImage' : p[i].GiveImage,
                        'State': p[i].State
                    }
                    list1.append(array)
            return list1
        else:
            array = {
                'msg': '信息为空',
                'state': '0',
                'num':0
            }
            list1 = [array]
            list1.append(array)
            return list1

    def givecomment(self):
        GiveId = int(request.args.get('GiveId'))
        g = Givecomment.query.filter_by(GiveId=GiveId).all()
        if len(g)>0:
            array = {
                'msg': '成功',
                'state': '1',
                'num':len(g)
            }
            d = data()
            list1 = [array]
            for i in range(0,len(g)):
                a = d.GetOthersData(g[i].UserId)
                array = {
                    'UserSex':a['UserSex'],
                    'UserPhoto':a['UserPhoto'],
                    'NickName':a['NickName'],
                    'UserId':g[i].UserId,
                    'CommentInformation':g[i].CommentInformation
                }
                list1.append(array)
                return list1
        else:
            array = {
                'msg':'当前没有评论，赶紧抢占沙发吧！',
                'state' :'0',
                'num':0
            }
            list1 = [array]
            list1.append(array)
            return list1

    def creat(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        file = request.files['photo']
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId

    def getgive(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId
                GiveId = int(form.get('GiveId'))
                CommentInformation = form.get('CommentInformation')
                if CommentInformation is None:
                    state = '0'
                    msg = '说出你想说的，获得礼物的几率更大哦'
                else:
                    c = Givecomment()
                    c.UserId = UserId
                    c.CommentInformation =CommentInformation
                    c.GiveId = GiveId
                    db.session.add(c)
                    db.session.commit()
                    state = '1'
                    msg = '成功'
            else:
                state = '0'
                msg = '请登录'
        else:
            state = '0'
            msg = '请登录'
        array = {
            'state':state,
            'msg':msg
        }
        return array

    def select(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                UserId = u.UserId
                GetUser = form.get('GetUser')
                GiveId = form.get('GiveId')
                g = Give.query.filter_by(GiveId = GiveId).first()
                if g.UserId == UserId:
                    g.GetUser = GetUser
                    g.State = 0
                    state = '1'
                    msg = '成功'
                else:
                    state = '0'
                    msg = '操作非法'
            else:
                state = '0'
                msg = '请登录'
        else:
            state = '0'
            msg = '请登录'
        array = {
            'state':state,
            'msg':msg
        }
        return array








