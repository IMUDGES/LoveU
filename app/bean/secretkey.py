# -*- coding:utf-8 -*-
import string, random, hashlib


class Secretkey():
    def GetSecretKey(self):
        str=string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 26)).replace(' ','')
        str1=hashlib.md5()
        str1.update(str)
        str1=str1.hexdigest()
        str2=hashlib.md5()
        str2.update(str1)
        str2=str2.hexdigest()
        return str2
