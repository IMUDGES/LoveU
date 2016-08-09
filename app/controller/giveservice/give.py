# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Give, db, Givecomment
from app.controller.service.data import data
from app.bean.upimage import upimage
from flask import session



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
            list1 = []
            for i in range(0, len(p)):
                if p[i] is not None:
                    a = d.GetOthersData(p[i].UserId)
                    array1 = {
                        'UserPhoto':a['UserPhoto'],
                        'UserSex':a['UserSex'],
                        'NickName':a['NickName'],
                        'GiveId': p[i].GiveId,
                        'UserId': p[i].UserId,
                        'GiveInformation': p[i].GiveInformation,
                        'GiveImage' : p[i].GiveImage,
                        'State': p[i].State
                    }
                    list1.append(array1)
            array['giveModels'] = list1
            return array
        else:
            array = {
                'msg': '信息为空',
                'state': '0',
                'num':0
            }
            return array

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
            list1 = []
            for i in range(0,len(g)):
                a = d.GetOthersData(g[i].UserId)
                array1 = {
                    'UserSex':a['UserSex'],
                    'UserPhoto':a['UserPhoto'],
                    'NickName':a['NickName'],
                    'UserId':g[i].UserId,
                    'CommentInformation':g[i].CommentInformation
                }
                list1.append(array1)
            array['givecommentdata'] = list1
            return list1
        else:
            array = {
                'msg':'当前没有评论，赶紧抢占沙发吧！',
                'state' :'0',
                'num':0
            }
            return array

#安卓图片处理

    def upgiveimage(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        file = request.files['GiveImage']
        # UserPhone = '2147483647'
        # SecretKey = '8fe98a41f795497799ef3ade6ee02366'
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.SecretKey == SecretKey:
                up = upimage()
                a = up.upuserphoto(file, 'give')
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
        up = self.upgiveimage()
        if up['state'] == '1':
            form = request.form
            if not form.get('GiveInformation') or not up['imageurl']:
                state = '0'
                msg = '请将信息填写完整'
            else:
                UserPhone = form.get('UserPhone')
                SecretKey = form.get('SecretKey')
                if UserPhone and SecretKey:
                    u = User.query.filter_by(UserPhone=UserPhone).first()
                    if u.SecretKey == SecretKey:
                        g = Give()
                        g.UserId = u.UserId
                        g.GiveInformation = form.get('GiveInformation')
                        g.GiveImage = up['imageurl']
                        g.State = 1
                        db.session.add(g)
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

###结束

#网站图片处理

    def Upgiveimage(self):
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
                a = up.upuserphoto(file, 'give')
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
        up = self.Upgiveimage()
        if up['state'] == '1':
            form = request.form
            if not form.get('GiveInformation') or not up['imageurl']:
                state = '0'
                msg = '请将信息填写完整'
            else:
                UserPhone = form.get('UserPhone')
                SecretKey = form.get('SecretKey')
                if UserPhone and SecretKey:
                    u = User.query.filter_by(UserPhone=UserPhone).first()
                    if u.SecretKey == SecretKey:
                        g = Give()
                        g.UserId = u.UserId
                        g.GiveInformation = form.get('GiveInformation')
                        g.GiveImage = up['imageurl']
                        g.State = 1
                        db.session.add(g)
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








