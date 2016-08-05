import multiprocessing
from datarun.datarunservice import Datarun

datarungo = Datarun()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=datarungo.runFood, args = (2,))
    p2 = multiprocessing.Process(target=datarungo.runHelp, args = (3,))
    p3 = multiprocessing.Process(target=datarungo.runPai, args = (4,))
    p4 = multiprocessing.Process(target=datarungo.runRun, args=(5,))
    p5 = multiprocessing.Process(target=datarungo.runXue, args=(6,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()