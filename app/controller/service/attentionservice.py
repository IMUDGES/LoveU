# -*- coding:utf-8 -*-
from app.db import Attention, db, User
from flask import request


class Attentionservice(object):
    def attention_other(self):
        try:
            form = request.form
            UserPhone = form.get('UserPhone')
            SecretKey = form.get('SecretKey')
            BefocusonId = form.get('BefocusonId')
            user = User.query.filter_by(UserPhone=UserPhone).first()
            if user.SecretKey == SecretKey:
                attentioninfo = Attention()
                attentioninfo.UserId = user['UserId']
                attentioninfo.BefocusonId  = BefocusonId
                db.session.add(attentioninfo)
                db.session.commit()
                array = {
                    'msg': '成功',
                    'state': '1'
                }
            else:
                array = {
                    'msg': '请登录',
                    'state': '0'
                }
            return array
        except Exception as e:
            array = {
                'msg': '出现未知的错误了请等等',
                'state': '0'
            }
            return array
