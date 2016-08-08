# -*- coding:utf-8 -*-
from app.config import ALLOWED_EXTENSIONS
from app.bean.qiniuup import Qiniuup
from werkzeug.utils import secure_filename
from app import app
from app.config import UPLOAD_FOLDER
import os
from app.bean.usetphotorandom import Userphotorandom

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class upimage(object):

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    def upuserphoto(self, file, Space):
        try:
            file.filename = file.filename
            if file and self.allowed_file(file.filename):
                qiniuup = Qiniuup()
                userphotorandom = Userphotorandom()
                # 图片名字
                file.filename = userphotorandom.getuserphotorandom() + '.png'
                fname = secure_filename(file.filename)

                file.save(os.path.join(UPLOAD_FOLDER, fname))
                print(UPLOAD_FOLDER + file.filename)
                str = qiniuup.up(UPLOAD_FOLDER + file.filename, Space)
                array = {
                    'state':'1',
                    'msg':'上传成功',
                    'url':str
                }
                return array
            else:
                msg = "请合法上传！"
                state = '0'
                array = {
                    'state': state,
                    'msg': msg,
                    'url': ''
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
