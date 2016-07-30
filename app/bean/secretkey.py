# -*- coding:utf-8 -*-
import string, random, hashlib
from app.bean.md5 import encrypt


class Secretkey():
    def GetSecretKey(self):
        str2=random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 26)
        str3 = ''
        for i in str2:
            str3 = str3 + i
        str4 = str3.encode('utf-8')
        psw = encrypt(str4)
        return psw
