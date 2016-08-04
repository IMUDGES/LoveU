from app.db import db, Give, Pai, Run, Xue, Food, Help
import datetime


ISOTIMEFORMAT = "%Y-%m-%d %H:%M:%S"
class Datarun(object):
    def getnowtime(self):
        date1= datetime.datetime.now()
        date2 = date1.strftime(ISOTIMEFORMAT)
        date3 = datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
        return date3

    def runRun(self):
        run = Run.query.all()
        for i in range(0, len(run)):
            if run[i].RunTime <= self.getnowtime():
                run[i].state = 0
                db.session.commit()

    def runXue(self):
        xue = Xue.query.all()
        for i in range(0,len(xue)):
            if xue[i].XueTime <= self.getnowtime():
                xue[i].state = 0
                db.session.commit()

    




