from app.db import Food, Help, Give, Run, Xue, Pai
from app.controller.service.data import data

class search():

    def searchfood(self, message):
        p = f = Food.query.filter(Food.FoodInformation.ilike('%'+message+'%')|Food.FoodTime.ilike('%'+message+'%')|Food.FoodArea.ilike('%'+message+'%')).filter_by(State=1).all()
        l = []
        d = data()
        for i in range(0, len(p)):
            if f[i] is not None:
                a = d.GetOthersData(p[i].UserId)
                array1 = {
                    'UserPhoto': a['UserPhoto'],
                    'NickName': a['NickName'],
                    'UserSex': a['UserSex'],
                    'FoodId': p[i].FoodId,
                    'UserId': p[i].UserId,
                    'FoodArea': p[i].FoodArea,
                    'FoodInformation': p[i].FoodInformation,
                    'GetUser': p[i].GetUser,
                    'FoodTime': p[i].FoodTime,
                    'FoodWay': p[i].FoodWay,
                    'State': p[i].State
                }
                l.append(array1)
        array = {
            'num': len(f),
            'foodlist': l
        }
        return array

    def searchrun(self, message):
        p = r = Run.query.filter(Run.RunInformation.ilike('%'+message+'%')|Run.RunTime.ilike('%'+message+'%')|Run.RunArea.ilike('%'+message+'%')).filter_by(State=1).all()
        d = data()
        list1 = []
        for i in range(0, len(p)):
            if p[i] is not None:
                a = d.GetOthersData(p[i].UserId)
                array1 = {
                    'UserPhoto': a['UserPhoto'],
                    'NickName': a['NickName'],
                    'UserSex': a['UserSex'],
                    'RunId': p[i].RunId,
                    'UserId': p[i].UserId,
                    'RunArea': p[i].RunArea,
                    'RunInformation': p[i].RunInformation,
                    'GetUser': p[i].GetUser,
                    'RunTime': p[i].RunTime,
                    'State': p[i].State
                }
                list1.append(array1)
        array = {
            'num': len(r),
            'runlist': list1
        }
        return array

    def searchpai(self, message):
        p = Pai.query.filter(Pai.PaiTitle.ilike('%' + message + '%') |Pai.PaiInformation.ilike('%' + message + '%') | Pai.PaiMoney.ilike('%' + message + '%')).filter_by(State=1).all()
        list1 = []
        d = data()
        for i in range(0, len(p)):
            if p[i] is not None:
                print(p[i].UserId)
                a = d.GetOthersData(p[i].UserId)
                array1 = {
                    'UserPhoto': a['UserPhoto'],
                    'NickName': a['NickName'],
                    'UserSex': a['UserSex'],
                    'PaiId': p[i].PaiId,
                    'PaiTitle': p[i].PaiTitle,
                    'UserId': p[i].UserId,
                    'PaiMoney': p[i].PaiMoney,
                    'UpTime': p[i].UpTime,
                    'PaiInformation': p[i].PaiInformation,
                    'PaiImage': p[i].PaiImage,
                    'DownTime': p[i].DownTime
                }
                list1.append(array1)
        array = {
            'num': len(p),
            'pailist': list1
        }
        return array

    def searchxue(self, message):
        p = x = Xue.query.filter(
            Xue.XueInformation.ilike('%' + message + '%') | Xue.XueTime.ilike('%' + message + '%') | Xue.XueArea.ilike(
                '%' + message + '%')).filter_by(State=1).all()
        d = data()
        list1 = []
        for i in range(0, len(p)):
            if p[i] is not None:
                a = d.GetOthersData(p[i].UserId)
                array1 = {
                    'UserPhoto': a['UserPhoto'],
                    'NickName': a['NickName'],
                    'UserSex': a['UserSex'],
                    'XueId': p[i].XueId,
                    'UserId': p[i].UserId,
                    'XueArea': p[i].XueArea,
                    'XueInformation': p[i].XueInformation,
                    'GetUser': p[i].GetUser,
                    'XueTime': p[i].XueTime,
                    'State': p[i].State
                }
                list1.append(array1)
        array = {
            'num': len(x),
            'xuelist': list1
        }
        return array

    def searchgive(self, message):
        p = g = Give.query.filter(Give.GiveInformation.ilike('%' + message + '%')).filter_by(State=1).all()
        d = data()
        list1 = []
        for i in range(0, len(p)):
            if p[i] is not None:
                a = d.GetOthersData(p[i].UserId)
                array1 = {
                    'UserPhoto': a['UserPhoto'],
                    'UserSex': a['UserSex'],
                    'NickName': a['NickName'],
                    'GiveId': p[i].GiveId,
                    'UserId': p[i].UserId,
                    'GiveInformation': p[i].GiveInformation,
                    'GiveImage': p[i].GiveImage,
                    'State': p[i].State
                }
                list1.append(array1)
        array = {
            'num': len(g),
            'givelist': list1
        }
        return array

    def searchhelp(self, message):
        p = h = Help.query.filter(Help.HelpInformation.ilike('%' + message + '%')).filter_by(State=1).all()
        d = data()
        list1 = []
        for i in range(0, len(p)):
            if p[i] is not None:
                a = d.GetOthersData(p[i].UserId)
                array1 = {
                    'UserPhoto': a['UserPhoto'],
                    'NickName': a['NickName'],
                    'UserSex': a['UserSex'],
                    'HelpId': p[i].HelpId,
                    'UserId': p[i].UserId,
                    'HelpInformation': p[i].HelpInformation,
                    'HelpMoney': p[i].HelpMoney,
                    'GetUser': p[i].GetUser,
                    'DownTime': p[i].DownTime,
                    'State': p[i].State
                }
                list1.append(array1)
        array = {
            'num': len(h),
            'helplist': list1
        }
        return array

    def searchall(self, message):
        array = {
            'state': 1,
            'msg': '成功',
            'food': self.searchfood(message),
            'run': self.searchrun(message),
            'pai': self.searchpai(message),
            'xue': self.searchxue(message),
            'give': self.searchgive(message),
            'help': self.searchhelp(message)
        }
        return array
