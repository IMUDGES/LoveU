# -*- coding:utf-8 -*-
from app.bean.secretkey import Secretkey
from app.db import User
from flask import request


class foodservice():
    def creat(self):
        Secretkey = request.args.get('SecretKey')
        UserPhone = request.args.get()
        if not Secretkey:


