# -*- coding:utf-8 -*-
from app.config import ALLOWED_EXTENSIONS
from app.bean.qiniuup import Qiniuup
from werkzeug.utils import secure_filename
from app import app
from app.config import UPLOAD_FOLDER
from app.db import db,User
import os

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Upphoto(object):
    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    def upuserphoto(self, file, UserPhone, SecretKey):
        try:
            if file and self.allowed_file(file.filename):
                qiniuup = Qiniuup()
                fname = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, fname))
                print(UPLOAD_FOLDER + file.filename)
                str = qiniuup.up(UPLOAD_FOLDER + file.filename, 'loveu')
                u = User.query.filter_by(UserPhone=UserPhone).first()
                if u.SecretKey == SecretKey:
                    u.UserPhoto = str
                    db.session.commit()
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
                state = '1'
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



