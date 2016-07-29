# -*- coding:utf-8 -*-
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

#此模块未完成
class Qiniuup(object):
    def up(self):
        q = Auth("gFO-8IYwjVPzNAmbAORHJCgGwIHzcyIbFhZ3yVIi", "hllClWcBETkcn0aI8SROEe4Y1blV5gEQwgUHAQQu")
        bucket_name = 'loveu'
        key = '图片名字';
        token = q.upload_token(bucket_name, key)
        localfile = '本地图片路径'
        ret, info = put_file(token, key, localfile)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)


