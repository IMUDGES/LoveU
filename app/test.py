from flask import request
from app.bean.upimage import upimage
import base64


def up():
    file = request.files.getlist('file')
    print('1')
    print (dir(file[0]))
    print (file[0].filename)
    print(file[0].name)
    print(file[0].stream)
    print(file[0].save)
    # file1 = request.files('file')
    up = upimage()
    a = up.upuserphoto(file[0],'give')
    return a['msg']

    # print('1')
    # print(request.form.get('msg'))
    # #file1 = request.form.get('file')
    # print (request.form)
    # print (file1)
    # file2 = file1.replace('data:image/png;base64,','')
    # file = base64.b64decode(file2)
    # # print (file)
    # # print(request.data)
    # # print(request.data())
    # #print (type(file))
    # # print('2')
    # up = upimage()
    # a = up.upuserphoto(file, 'give')
    # if a['state'] == '1':
    #     state = '1'
    #     msg = '上传成功'
    # else:
    #     state = '0'
    #     msg = a['msg']
    # array = {
    #     'state':state,
    #     'msg':msg
    # }
    # print (state)
    # return array
