import httplib2
import string


def GetCookies():
    conn  = httplib2.Http()
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'	keep-alive',
        'Host':'jwxt.imu.edu.cn',
        'Referer':'http://jwxt.imu.edu.cn/',
        'User-Agent':'	Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    c1,c = conn.request('http://jwxt.imu.edu.cn/loginAction.do?zjh=0151122350&mm=15248113901','GET',headers=header)
    print (c1)
    str = c.decode('gb2312')
    if "请输入账号" in str:
        cookie = c1['set-cookie'].replace('; path=/','')
    #cookie = cookie.replace('JSESSIONID=','')
    return cookie
def xuanke(k_num,k_id):
    conn = httplib2.Http()
    cookie = GetCookies()
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': '	keep-alive',
        'Cookie':cookie,
        'Host': 'jwxt.imu.edu.cn',
        'Referer': 'http://jwxt.imu.edu.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }
    conn.request('http://jwxt.imu.edu.cn/xkAction.do?actionType=-1&fajhh=32874','GET',headers=header)
    conn.request('http://jwxt.imu.edu.cn/xkAction.do?actionType=2&pageNumber=-1&oper1=ori','GET',headers=header)
    conn.request('http://jwxt.imu.edu.cn/xkAction.do?actionType=5&pageNumber=-1&cx=ori','GET',headers=header)
    conn.request('http://jwxt.imu.edu.cn/xkAction.do?kch=140442220&cxkxh=&kcm=&skjs=&kkxsjc=&skxq=&skjc=&pageNumber=-2&preActionType=2&actionType=5', 'GET', headers=header)
    c,c1 = conn.request('http://jwxt.imu.edu.cn/xkAction.do?kcId='+k_num+ '_' + k_id + '&preActionType=5&actionType=9','GET',headers=header)
GetCookies()


