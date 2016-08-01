# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Give, db, Givecomment



class giveservice():

    def give(self):
        page = int(request.args.get('page'))
        # SecretKey = '0a6b58441e5069288e0f95939a2c4375'
        # UserPhone = '2147483647'
        # page = 1
        f = Give.query.filter_by(State=1).paginate(page, 10, False)
        p = f.items
        if p is not None:
            array = {
                'msg': '成功',
                'state': '1'
            }
            list1 = [array]
            for i in range(0, len(p)):
                if p[i] is not None:
                    array = {
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
                'state': '0'
            }
            return array

    def givecomment(self):
        GiveId = request.args.get('GiveId')
        print(GiveId)
        g = GiveComment.query.filter_by(GiveId=GiveId).first()
        print (g)
        if g is not None:
            array = {
                'msg': '成功',
                'state': '1'
            }
            list1 = [array]
            for i in range(0,len(g)):
                array = {
                    'UserId':g[i].UserId,
                    'CommentInformation':g[i].CommentInformation
                }
                list1.append(array)
            return list1
        else:
            array = {
            'msg':'当前没有评论，赶紧抢占沙发吧！',
            'state' :'0'
            }
            return array
