# -*- coding:utf-8 -*-
import string, random, hashlib


class Secretkey():
    def GetSecretKey(self):
        str2=random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 26)
        str3 = ''
        for i in str2:
            str3 = str3 + i
        str4 = str3.encode('utf-8')
        m = hashlib.md5()
        m.update(str4)
        psw = m.hexdigest()
        return psw