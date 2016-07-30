# -*- coding:utf-8 -*-
from app.config import ALLOWED_EXTENSIONS

class Upphoto(object):
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


