# -*- coding:utf-8 -*-
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
from app.bean.usetphotorandom import Userphotorandom

#此模块未完成
class Qiniuup(object):
    def up(self,imagelocation,bucketname):
        q = Auth("gFO-8IYwjVPzNAmbAORHJCgGwIHzcyIbFhZ3yVIi", "hllClWcBETkcn0aI8SROEe4Y1blV5gEQwgUHAQQu")
        bucket_name = bucketname
        userphotorandom = Userphotorandom()
        #图片名字
        key = userphotorandom.getuserphotorandom()
        token = q.upload_token(bucket_name, key)
        localfile = imagelocation
        ret, info = put_file(token, key, localfile)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)
        print(key)
        return "http://7xrqhs.com1.z0.glb.clouddn.com/" + key

