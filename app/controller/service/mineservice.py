from app.controller.foodservice.food import foodservice
from app.controller.helpservice.help import helpservice
from app.controller.giveservice.give import giveservice
from app.controller.runservice.run import runservice
from  app.controller.xueservice.xue import xueservice
from app.controller.paiservice.pai import paiservice


def mine(User_Phone,Secret_Key):
    f = foodservice()
    h = helpservice()
    g = giveservice()
    r = runservice()
    x = xueservice()
    p = paiservice()
    array = {}
    array1 = {}
    #获取food
    fa = {}
    fa_issue = {}
    fa_get = {}
    fa_issue['myissuefood_notoverdue'] = f.my_issuefood(1,User_Phone, Secret_Key)
    fa_issue['myissuefood_overdue'] = f.my_issuefood(0, User_Phone, Secret_Key)
    fa_get['mygetfood_notoverdue'] = f.my_getfood(1,User_Phone, Secret_Key)
    fa_get['mygetfood_overdue'] = f.my_getfood(0,User_Phone, Secret_Key)
    fa['myissuefood'] = fa_issue
    fa['mygetfood'] = fa_get
    #获取help
    ha = {}
    ha_issue = {}
    ha_get = {}
    ha_issue['myissuehelp_notoverdue'] = h.my_issuehelp(1, User_Phone, Secret_Key)
    ha_issue['myissuehelp_overdue'] = h.my_issuehelp(0, User_Phone, Secret_Key)
    ha_get['mygethelp_notoverdue'] = h.my_gethelp(1, User_Phone, Secret_Key)
    ha_get['mygethelp_overdue'] = h.my_gethelp(0, User_Phone, Secret_Key)
    ha['myissuehelp'] = ha_issue
    ha['mygethelp'] = ha_get
    #获取give
    ga = {}
    ga_issue = {}
    ga_get = {}
    ga_issue['myissuegive_notoverdue'] = g.my_issuegive(1, User_Phone, Secret_Key)
    ga_issue['myissuegive_overdue'] = g.my_issuegive(0, User_Phone, Secret_Key)
    ga_get['mygetgive_notoverdue'] = g.my_getgive(1, User_Phone, Secret_Key)
    ga_get['mygetgive_overdue'] = g.my_getgive(0, User_Phone, Secret_Key)
    ga['myissuegive'] = ga_issue
    ga['mygetgive'] = ga_get
    #获取pai
    pa = {}
    pa_issue = {}
    pa_get = {}
    pa_issue['myissuepai_notoverdue'] = p.my_issuepai(1, User_Phone, Secret_Key)
    pa_issue['myissuepai_overdue'] = p.my_issuepai(0, User_Phone, Secret_Key)
    pa_get['mygetpai_notoverdue'] = p.my_getpai(1, User_Phone, Secret_Key)
    pa_get['mygetpai_overdue'] = p.my_getpai(0, User_Phone, Secret_Key)
    pa['myissuepai'] = pa_issue
    pa['mygetpai'] = pa_get
    #获取run
    ra = {}
    ra_issue = {}
    ra_get = {}
    ra_issue['myissuerun_notoverdue'] = r.my_issuerun(1, User_Phone, Secret_Key)
    ra_issue['myissuerun_overdue'] = r.my_issuerun(0, User_Phone, Secret_Key)
    ra_get['mygetrun_notoverdue'] = r.my_getrun(1, User_Phone, Secret_Key)
    ra_get['mygetrun_overdue'] = r.my_getrun(0, User_Phone, Secret_Key)
    ra['myissuerun'] = pa_issue
    ra['mygetrun'] = pa_get
    #获取xue
    xa = {}
    xa_issue = {}
    xa_get = {}
    xa_issue['myissuexue_notoverdue'] = x.my_issuexue(1, User_Phone, Secret_Key)
    xa_issue['myissuexue_overdue'] = x.my_issuexue(0, User_Phone, Secret_Key)
    xa_get['mygetxue_notoverdue'] = x.my_getxue(1, User_Phone, Secret_Key)
    xa_get['mygetxue_overdue'] = x.my_getxue(0, User_Phone, Secret_Key)
    xa['myissuexue'] = pa_issue
    xa['mygetxue'] = pa_get
    #返回issue结果
    array = {
        'state':'1',
        'msg':'成功'
    }
    array['myissuefood_notoverdue'] = fa_issue['myissuefood_notoverdue']['data']
    array['myissuefood_overdue'] = fa_issue['myissuefood_overdue']['data']
    array['myissuehelp_notoverdue'] = ha_issue['myissuehelp_notoverdue']['data']
    array['myissuehelp_overdue'] = ha_issue['myissuehelp_overdue']['data']
    array['myissuegive_notoverdue'] = ga_issue['myissuegive_notoverdue']['data']
    array['myissuegive_overdue'] = ga_issue['myissuegive_overdue']['data']
    array['myissuepai_notoverdue'] = pa_issue['myissuepai_notoverdue']['data']
    array['myissuepai_overdue'] = pa_issue['myissuepai_overdue']['data']
    array['myissuerun_notoverdue'] = ra_issue['myissuerun_notoverdue']['data']
    array['myissuerun_overdue'] = ra_issue['myissuerun_overdue']['data']
    array['myissuexue_notoverdue'] = xa_issue['myissuexue_notoverdue']['data']
    array['myissuexue_overdue'] = xa_issue['myissuexue_overdue']['data']
    array['myissuefood_notoverdue_num'] = fa_issue['myissuefood_notoverdue']['num']
    array['myissuefood_overdue_num'] = fa_issue['myissuefood_overdue']['num']
    array['myissuehelp_notoverdue_num'] = ha_issue['myissuehelp_notoverdue']['num']
    array['myissuehelp_overdue_num'] = ha_issue['myissuehelp_overdue']['num']
    array['myissuegive_notoverdue_num'] = ga_issue['myissuegive_notoverdue']['num']
    array['myissuegive_overdue_num'] = ga_issue['myissuegive_overdue']['num']
    array['myissuepai_notoverdue_num'] = pa_issue['myissuepai_notoverdue']['num']
    array['myissuepai_overdue_num'] = pa_issue['myissuepai_overdue']['num']
    array['myissuerun_notoverdue_num'] = ra_issue['myissuerun_notoverdue']['num']
    array['myissuerun_overdue_num'] = ra_issue['myissuerun_overdue']['num']
    array['myissuexue_notoverdue_num'] = xa_issue['myissuexue_notoverdue']['num']
    array['myissuexue_overdue_num'] = xa_issue['myissuexue_overdue']['num']
    #返回get结果
    array1 = {
        'state': '1',
        'msg': '成功'
    }
    array1['mygetfood_notoverdue'] = fa_get['mygetfood_notoverdue']['data']
    array1['mygetfood_overdue'] = fa_get['mygetfood_overdue']['data']
    array1['mygethelp_notoverdue'] = ha_get['mygethelp_notoverdue']['data']
    array1['mygethelp_overdue'] = ha_get['mygethelp_overdue']['data']
    array1['mygetgive_notoverdue'] = ga_get['mygetgive_notoverdue']['data']
    array1['mygetgive_overdue'] = ga_get['mygetgive_overdue']['data']
    array1['mygetpai_notoverdue'] = pa_get['mygetpai_notoverdue']['data']
    array1['mygetpai_overdue'] = pa_get['mygetpai_overdue']['data']
    array1['mygetrun_notoverdue'] = ra_get['mygetrun_notoverdue']['data']
    array1['mygetrun_overdue'] = ra_get['mygetrun_overdue']['data']
    array1['mygetxue_notoverdue'] = xa_get['mygetxue_notoverdue']['data']
    array1['mygetxue_overdue'] = xa_get['mygetxue_overdue']['data']
    array1['mygetfood_notoverdue_num'] = fa_get['mygetfood_notoverdue']['num']
    array1['mygetfood_overdue_num'] = fa_get['mygetfood_overdue']['num']
    array1['mygethelp_notoverdue_num'] = ha_get['mygethelp_notoverdue']['num']
    array1['mygethelp_overdue_num'] = ha_get['mygethelp_overdue']['num']
    array1['mygetgive_notoverdue_num'] = ga_get['mygetgive_notoverdue']['num']
    array1['mygetgive_overdue_num'] = ga_get['mygetgive_overdue']['num']
    array1['mygetpai_notoverdue_num'] = pa_get['mygetpai_notoverdue']['num']
    array1['mygetpai_overdue_num'] = pa_get['mygetpai_overdue']['num']
    array1['mygetrun_notoverdue_num'] = ra_get['mygetrun_notoverdue']['num']
    array1['mygetrun_overdue_num'] = ra_get['mygetrun_overdue']['num']
    array1['mygetxue_notoverdue_num'] = xa_get['mygetxue_notoverdue']['num']
    array1['mygetxue_overdue_num'] = xa_get['mygetxue_overdue']['num']
    return array,array1


