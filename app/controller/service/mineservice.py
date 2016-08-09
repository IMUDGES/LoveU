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
    #获取food
    fa = {}
    faissue = {}
    faget = {}
    faissue['myissuefood_notoverdue'] = f.my_issuefood(1,User_Phone, Secret_Key)
    faissue['myissuefood_overdue'] = f.my_issuefood(0, User_Phone, Secret_Key)
    faget['mygetfood_notoverdue'] = f.my_getfood(1,User_Phone, Secret_Key)
    faget['mygetfood_overdue'] = f.my_getfood(0,User_Phone, Secret_Key)
    fa['myissuefood'] = faissue
    fa['mygetfood'] = faget
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
    array['food'] = fa
    array['help'] = ha
    array['give'] = ga
    array['pai'] = pa
    array['run'] = ra
    array['xue'] = xa
    return array


