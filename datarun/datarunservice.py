from app.db import db, Give, Pai, Run, Xue, Food, Help
import datetime
import time


ISOTIMEFORMAT = "%Y-%m-%d %H:%M:%S"
class Datarun(object):
    def getnowtime(self):
        date1= datetime.datetime.now()
        date2 = date1.strftime(ISOTIMEFORMAT)
        date3 = datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
        return date3

    def runRun(self,interval):
        run = Run.query.all()
        time.sleep(interval)
        while(True):
            print("rungo")
            #time.sleep(interval)
            for i in range(0, len(run)):
                if run[i].RunTime <= self.getnowtime():
                    run[i].State = 0
                    db.session.commit()

    def runXue(self,interval):
        xue = Xue.query.all()
        time.sleep(interval)
        while (True):
            print("xuego")
            #time.sleep(interval)
            for i in range(0,len(xue)):
                if xue[i].XueTime <= self.getnowtime():
                    xue[i].State = 0
                    db.session.commit()

    def runFood(self,interval):
        food = Food.query.all()
        time.sleep(interval)
        while (True):
            print("foodgo")
            #time.sleep(interval)
            for i in range(0,len(food)-1):
                if food[i].FoodTime <= self.getnowtime():
                    food[i].State = 0
                    db.session.commit()

    def runHelp(self,interval):
        help = Help.query.all()
        time.sleep(interval)
        while (True):
            print("helpgo")
            #time.sleep(interval)
            for i in range(0,len(help)):
                if help[i].DownTime <= self.getnowtime():
                    help[i].Finish = 1
                    db.session.commit()

    def runPai(self,interval):
        pai = Pai.query.all()
        time.sleep(interval)
        while (True):
            print("paigo")
            #time.sleep(interval)
            for i in range(0,len(pai)):
                if pai[i].DownTime <= self.getnowtime():
                    pai[i].State = 0
                    db.session.commit()



