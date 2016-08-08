# -*- coding:utf-8 -*-
from app.db import Refuse, db, User
from flask import request


class Refuseservice(object):
    def refuse_other(self):
        try:
            UserPhone = request.args.get('UserPhone')
            OtherUserId = request.args.get('OtherUserId')
            user = User.query.filter_by(UserPhone=UserPhone).first()
            refuseinfo = Refuse()
            refuseinfo.UserId = user['UserId']
            refuseinfo.BeRefuseId = OtherUserId
            db.session.add(refuseinfo)
            db.session.commit()
            array = {
                'msg': '成功',
                'state': '1'
            }
            return array
        except Exception as e:
            array = {
                'msg': '出现未知的错误了请等等',
                'state': '0'
            }
            return array
