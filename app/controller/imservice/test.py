import os
from app.bean.rong import ApiClient


app_key = 'y745wfm8440uv'
app_secret = '8H4Zs6MenT3Trf'
api = ApiClient(app_key, app_secret)
r = api.getToken(userId='1', name='nickname', portraitUri='http://7xrqhs.com1.z0.glb.clouddn.com/b932e5c1bd178fc3eb96792d3bfcf2fd?imageView2/0/w/96/h/96/format/png/interlace/1/')

print(r)
