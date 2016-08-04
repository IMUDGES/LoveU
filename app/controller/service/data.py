from flask import request
from app.db import User


class data():

    def GetOthersData(self,UserId):
        u = User.query.filter_by(UserId = UserId).first()
        if u is not None:
            array = {
                'msg' : '成功',
                'state' : '1',
                'UserId' : u.UserId,
                'NickName' : u.NickName,
                'UserSex' : u.UserSex,
                'UserPhoto' : u.UserPhoto
            }
            return array
        else:
            array = {
                'msg' : '不存在此ID',
                'state' : '0'
            }
            return array

    def GetMyData(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                array = {
                    'state' : '1',
                    'msg' : '成功',
                    'UserId': u.UserId,
                    'UserPhone' : u.UserPhone,
                    'NickName': u.NickName,
                    'TrueName' : u.TrueName,
                    'UserSex': u.UserSex,
                    'UserGrade' : u.UserGrade,
                    'UserPhoto': u.UserPhoto,
                    'UserMajor' : u.UserMajor
                }
                return array
            else:
                array = {
                    'state': '0',
                    'msg': '不存在此ID',
                }
                return array
        else:
            array = {
                'state': '0',
                'msg': '不存在此ID',
            }
            return array
