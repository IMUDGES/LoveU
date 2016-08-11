# -*- coding:utf-8 -*-
from flask import request, session
from app.db import User, Money, db
from app.db import Pai, Paicomment
from app.controller.moneyservice.money import moneyservice
from app.controller.service.data import data
from app.bean.upimage import upimage
import time

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
            list1 = []
            d = data()
            for i in range(0, len(p)):
                if p[i] is not None:
                    print(p[i].UserId)
                    a = d.GetOthersData(p[i].UserId)
                    array1 = {
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
                    list1.append(array1)
            array['paidata'] = list1
            return array
        else:
            array = {
                'num':0,
                'msg': '信息为空',
                'state': '0'
            }
            return array

#安卓图片处理

    def uppaiimage(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        file = request.files['PaiImage']
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                up = upimage()
                a = up.upuserphoto(file,'paimai')
                if a['state'] == '1':
                    state = '1'
                    msg = '上传成功'
                    imageurl = a['url']
                else:
                    state = '0'
                    msg = a['msg']
                    imageurl = ''
            else:
                state = '0'
                msg = '请登录'
                imageurl = ''
        else:
            state = '0'
            msg = '请登录'
            imageurl = ''
        array = {
            'state':state,
            'msg':msg,
            'imageurl':imageurl
        }
        return array

    def creat(self):
        up = self.uppaiimage()
        if up['state'] == '1':
            form = request.form
            if not form.get('DownTime') or not form.get('PaiInformation') or not up['imageurl'] or not form.get('PaiTitle'):
                state = '0'
                msg = '拍卖信息不完整'
            else:
                UserPhone = form.get('UserPhone')
                SecretKey = form.get('SecretKey')
                if UserPhone and SecretKey:
                    u = User.query.filter_by(UserPhone=UserPhone).first()
                    if u.SecretKey == SecretKey:
                        p = Pai()
                        p.UserId = u.UserId
                        p.PaiMoney = 1
                        p.UpTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
                        p.DownTime = form.get('DownTime')
                        p.PaiInformation = form.get('PaiInformation')
                        p.PaiImage = up['imageurl']
                        p.PaiTitle = form.get('PaiTitle')
                        p.State = 1
                        db.session.add(p)
                        db.session.commit()
                        state = '1'
                        msg = '创建成功'
                    else:
                        state = '0'
                        msg = '请登录'
                else:
                    state = '0'
                    msg = '请登录'
        else:
            state = up['state']
            msg = up['msg']
        array = {
            'state':state,
            'msg':msg
        }
        return array

###

#网站图片处理

    def Uppaiimage(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        file = request.files.getlist('file')
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                up = upimage()
                a = up.upuserphoto(file[0], 'paimai')
                if a['state'] == '1':
                    state = '1'
                    msg = '上传成功'
                    imageurl = a['url']
                else:
                    state = '0'
                    msg = a['msg']
                    imageurl = ''
            else:
                state = '0'
                msg = '请登录'
                imageurl = ''
        else:
            state = '0'
            msg = '请登录'
            imageurl = ''
        array = {
            'state': state,
            'msg': msg,
            'imageurl': imageurl
        }
        return array

    def Creat(self):
        up = self.Uppaiimage()
        if up['state'] == '1':
            form = request.form
            if not form.get('DownTime') or not form.get('PaiInformation') or not up['imageurl'] or not form.get(
                    'PaiTitle'):
                state = '0'
                msg = '拍卖信息不完整'
            else:
                UserPhone = form.get('UserPhone')
                SecretKey = form.get('SecretKey')
                if UserPhone and SecretKey:
                    u = User.query.filter_by(UserPhone=UserPhone).first()
                    if u.SecretKey == SecretKey:
                        p = Pai()
                        p.UserId = u.UserId
                        p.PaiMoney = 1
                        p.UpTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                        p.DownTime = form.get('DownTime')
                        p.PaiInformation = form.get('PaiInformation')
                        p.PaiImage = up['imageurl']
                        p.PaiTitle = form.get('PaiTitle')
                        p.State = 1
                        db.session.add(p)
                        db.session.commit()
                        state = '1'
                        msg = '创建成功'
                    else:
                        state = '0'
                        msg = '请登录'
                else:
                    state = '0'
                    msg = '请登录'
        else:
            state = up['state']
            msg = up['msg']
        array = {
            'state': state,
            'msg': msg
        }
        return array

###

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
            list1 = []
            d = data()
            for i in range(0, len(pc)):
                if len(pc)>0:
                    a = d.GetOthersData(pc[i].UserId)
                    array1 = {
                        'UserPhoto': a['UserPhoto'],
                        'NickName': a['NickName'],
                        'UserSex':a['UserSex'],
                        'CommentId':pc[i].CommentId,
                        'CommentInformation':pc[i].CommentInformation,
                        'PaiId':pc[i].PaiId
                    }
                    list1.append(array1)
            array['paicommentdata'] = list1
            return array
        else:
            array = {
                'msg': '失败',
                'state': '0',
                'num': 0
            }
            return array

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

    def my_issuepai(self, state, User_Phone, Secret_Key):
        UserPhone = User_Phone
        SecretKey = Secret_Key
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Pai.query.filter_by(UserId=u.UserId, State=state).all()
                if p is not None:
                    array = {
                        'msg': '成功',
                        'state': '1',
                        'num':len(p)
                    }
                    list1 = []
                    d = data()
                    for i in range(0, len(p)):
                        a = d.GetOthersData(p[i].UserId)
                        array1 = {
                            'UserPhoto': a['UserPhoto'],
                            'NickName': a['NickName'],
                            'UserSex': a['UserSex'],
                            'PaiId': p[i].PaiId,
                            'PaiTitle': p[i].PaiTitle,
                            'UserId': p[i].UserId,
                            'PaiMoney': p[i].PaiMoney,
                            'UpTime': p[i].UpTime,
                            'PaiInformation': p[i].PaiInformation,
                            'PaiImage': p[i].PaiImage,
                            'DownTime': p[i].DownTime
                        }
                        list1.append(array1)
                    array['paidata'] = list1
                else:
                    array = {
                        'msg': '信息为空',
                        'state': '0',
                        'num': 0,
                        'paidata': []
                    }
            else:
                array = {
                    'msg': '请登录',
                    'state': '0',
                    'num':0,
                    'paidata': []
                }
        else:
            array = {
                'msg': '请登录',
                'state': '0',
                'num': 0,
                'paidata': []
            }
        return array

    def my_getpai(self, state, User_Phone, Secret_Key):
        UserPhone = User_Phone
        SecretKey = Secret_Key
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                p = Pai.query.filter_by(GetUser=u.UserId, State=state).all()
                if p is not None:
                    array = {
                        'msg': '成功',
                        'state': '1',
                        'num':len(p)
                    }
                    list1 = []
                    d = data()
                    for i in range(0, len(p)):
                        a = d.GetOthersData(p[i].UserId)
                        array1 = {
                            'UserPhoto': a['UserPhoto'],
                            'NickName': a['NickName'],
                            'UserSex': a['UserSex'],
                            'PaiId': p[i].PaiId,
                            'PaiTitle': p[i].PaiTitle,
                            'UserId': p[i].UserId,
                            'PaiMoney': p[i].PaiMoney,
                            'UpTime': p[i].UpTime,
                            'PaiInformation': p[i].PaiInformation,
                            'PaiImage': p[i].PaiImage,
                            'DownTime': p[i].DownTime
                        }
                        list1.append(array1)
                    array['paidata'] = list1
                else:
                    array = {
                        'msg': '信息为空',
                        'state': '0',
                        'num': 0,
                        'paidata': []
                    }
            else:
                array = {
                    'msg': '请登录',
                    'state': '0',
                    'num':0,
                    'paidata': []
                }
        else:
            array = {
                'msg': '请登录',
                'state': '0',
                'num': 0,
                'paidata': []
            }
        return array

    def thispai(self):
        PaiId = int(request.args.get('PaiId'))
        p = Pai.query.filter_by(PaiId=PaiId).first()
        if p is not None:
            d = data()
            a =  d.GetOthersData(p.UserId)
            array = {
                'UserPhoto':a['UserPhoto'],
                'NickName':a['NickName'],
                'UserSex':a['UserSex'],
                'PaiId': p.PaiId,
                'PaiTitle': p.PaiTitle,
                'UserId': p.UserId,
                'PaiMoney': p.PaiMoney,
                'UpTime': p.UpTime,
                'PaiInformation': p.PaiInformation,
                'PaiImage': p.PaiImage,
                'DownTime': p.DownTime
            }
            state = '1'
            msg = '成功'
            ar = {
                'stata':state,
                'msg':msg
            }
            ar['paidata'] = array
            return ar
        else:
            array = {
                'state':'0',
                'msg':'不存在此信息'
            }
            return array











