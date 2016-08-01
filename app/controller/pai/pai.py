# -*- coding:utf-8 -*-
from flask import request
from app.db import User, Money, db
from app.db import Pai


class paiservice():

    def pai(self):
        page = request.args.get('page')
        P = Pai.query.filter_by(State=1).paginate(page,10,False)
        p = P.items
        if p is not None:
            array = {
                'msg': '成功',
                'state': '1'
            }
            list1 = [array]
            for i in range(0, len(p)):
                if p[i] is not None:
                    array = {
                        'PaiId': p[i].FoodId,
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
                'msg': '信息为空',
                'state': '0'
            }
            return array

    def get(self):
        pass

