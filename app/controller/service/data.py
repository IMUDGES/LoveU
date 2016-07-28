from flask import request
from app.db import User


class data():
    def GetOthersData(self):
        UserId = request.args.get('UserId')
        u = User.query.filter_by(UserId = UserId).first()
        array = {
            'UserId' : u.UserId,
            'NickName' : u.NickName,
            'UserSex' : u.UserSex,
            'UserPhoto' : u.UserPhoto
        }
        return array
    def GetMyData(self):
        UserPhone = request.args.get('UserPhone')
        SecretKey = request.args.get('SecretKey')
        if UserPhone and SecretKey:
            u = User.query.filter_by(UserPhone = UserPhone).first()
            if u.SecretKey == SecretKey:
                array = {
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
                return None
        else:
            return None
