from flask import request
from app.db import User
from app.db import Money


class data():

    def GetOthersData(self, UserId):
        u = User.query.filter_by(UserId=UserId).first()
        if u is not None:
            array = {
                'msg': '成功',
                'state': '1',
                'UserId': u.UserId,
                'NickName': u.NickName,
                'UserSex': u.UserSex,
                'UserPhoto': u.UserPhoto
            }
            return array
        else:
            array = {
                'msg': '不存在此ID',
                'state': '0'
            }
            return array

    def GetMyData(self):
        form = request.form
        UserPhone = form.get('UserPhone')
        SecretKey = form.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone=UserPhone).first()
            if u.UserGrade is None:
                isjwxt = '0'
                a = {
                    'isjwxt': isjwxt
                }
            else:
                isjwxt = '1'
                a ={
                    'isjwxt':isjwxt
                }
                a['TrueName'] = u.TrueName
                a['UserGrade'] = u.UserGrade
                a['UserMajor'] = u.UserMajor
            if u.SecretKey == SecretKey:
                m = Money.query.filter_by(UserId=u.UserId).first()
                if m is not None:
                    array = {
                        'state': '1',
                        'msg': '成功',
                        'ispay': '1',
                        'money':m.Money
                    }
                else:
                    array = {
                        'state': '1',
                        'msg': '成功',
                        'ispay': '0',
                        'money':0
                    }
                a = {
                    'UserId': u.UserId,
                    'UserPhone': u.UserPhone,
                    'NickName': u.NickName,
                    'UserPhoto': u.UserPhoto,
                    'UserSex': u.UserSex
                }
                array['data'] = a
                return array
            else:
                array = {
                    'state': '0',
                    'msg': '不存在此ID'
                }
                return array
        else:
            array = {
                'state': '0',
                'msg': '不存在此ID'
            }
            return array
