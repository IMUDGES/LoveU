# -*- coding:utf-8 -*-
from flask import request
from app.db import Help


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
