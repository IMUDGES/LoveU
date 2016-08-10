# -*- coding:utf-8 -*-
from app.config import ALLOWED_EXTENSIONS
from app.bean.qiniuup import Qiniuup
from werkzeug.utils import secure_filename
from app import app
from app.config import UPLOAD_FOLDER
from app.db import db,User
import os
from app.bean.usetphotorandom import Userphotorandom
from app.bean.rong import ApiClient

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Upphoto(object):

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#安卓头像处理
    def upuserphoto(self, file, UserPhone, SecretKey):
        try:
            if file and self.allowed_file(file.filename):
                qiniuup = Qiniuup()
                userphotorandom = Userphotorandom()
                # 图片名字
                file.filename = userphotorandom.getuserphotorandom()
                fname = secure_filename(file.filename)

                file.save(os.path.join(UPLOAD_FOLDER, fname))
                print(UPLOAD_FOLDER + file.filename)
                str = qiniuup.up(UPLOAD_FOLDER + file.filename, 'loveu')
                u = User.query.filter_by(UserPhone=UserPhone).first()
                if u.SecretKey == SecretKey:
                    u.UserPhoto = str
                    db.session.commit()
                    app_key = 'y745wfm8440uv'
                    app_secret = '8H4Zs6MenT3Trf'
                    api = ApiClient(app_key, app_secret)
                    db.session.commit()
                    r = api.refreshUser(u.UserId, u.NickName, u.UserPhoto)
                    msg = "成功！"
                    state = '1'
                    array = {
                        'state': state,
                        'msg': msg
                    }
                    return array
                else:
                    msg = '请登录'
                    state = '0'
                    array = {
                        'state': state,
                        'msg': msg
                    }
                    return array
            else:
                msg = "请合法上传！"
                state = '0'
                array = {
                    'state': state,
                    'msg': msg
                }
                return array
        except Exception as e:
            state = 0
            msg = "出现未知的错误了哦~，再试试吧"
            array = {
                'state': state,
                'msg': msg
            }
            return array
###

#网站头像处理
    def Upuserphoto(self, file, UserPhone, SecretKey):
        try:
            file.filename = file.filename + '.png'
            if file and self.allowed_file(file.filename):
                qiniuup = Qiniuup()
                userphotorandom = Userphotorandom()
                # 图片名字
                file.filename = userphotorandom.getuserphotorandom() + '.png'
                fname = secure_filename(file.filename)

                file.save(os.path.join(UPLOAD_FOLDER, fname))
                print(UPLOAD_FOLDER + file.filename)
                str = qiniuup.up(UPLOAD_FOLDER + file.filename, 'loveu')
                u = User.query.filter_by(UserPhone=UserPhone).first()
                if u.SecretKey == SecretKey:
                    u.UserPhoto = str
                    db.session.commit()
                    app_key = 'y745wfm8440uv'
                    app_secret = '8H4Zs6MenT3Trf'
                    api = ApiClient(app_key, app_secret)
                    db.session.commit()
                    r = api.refreshUser(u.UserId, u.NickName, u.UserPhoto)
                    msg = "成功！"
                    state = '1'
                    array = {
                        'state': state,
                        'msg': msg
                    }
                    return array
                else:
                    msg = '请登录'
                    state = '0'
                    array = {
                        'state': state,
                        'msg': msg
                    }
                    return array
            else:
                msg = "请合法上传！"
                state = '0'
                array = {
                    'state': state,
                    'msg': msg
                }
                return array
        except Exception as e:
            state = 0
            msg = "出现未知的错误了哦~，再试试吧"
            array = {
                'state': state,
                'msg': msg
            }
            return array
###



