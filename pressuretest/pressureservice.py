import multiprocessing
import httplib2
import time

def gofood(interval):
    conn = httplib2.Http()
    time.sleep(interval)
    while(True):
        resp, content = conn.request('http://183.175.14.250:5000/help?page=1',"GET")
        if resp:
            print("go")
        else:
            print("fail")
            break
            print("1111111111111111111111111111111111111111111111111111111111111111111111111111")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=gofood, args=(2,))
    p2 = multiprocessing.Process(target=gofood, args=(3,))
    p3 = multiprocessing.Process(target=gofood, args=(4,))
    p4 = multiprocessing.Process(target=gofood, args=(5,))
    p5 = multiprocessing.Process(target=gofood, args=(6,))
    p6 = multiprocessing.Process(target=gofood, args=(7,))
    p7 = multiprocessing.Process(target=gofood, args=(8,))
    p8 = multiprocessing.Process(target=gofood, args=(9,))
    p9 = multiprocessing.Process(target=gofood, args=(10,))
    p10 = multiprocessing.Process(target=gofood, args=(11,))
    p11 = multiprocessing.Process(target=gofood, args=(12,))
    p12 = multiprocessing.Process(target=gofood, args=(13,))
    p13 = multiprocessing.Process(target=gofood, args=(14,))
    p14 = multiprocessing.Process(target=gofood, args=(15,))
    p15 = multiprocessing.Process(target=gofood, args=(16,))
    p16 = multiprocessing.Process(target=gofood, args=(17,))
    p17 = multiprocessing.Process(target=gofood, args=(18,))
    p18 = multiprocessing.Process(target=gofood, args=(19,))
    p19 = multiprocessing.Process(target=gofood, args=(20,))
    p20 = multiprocessing.Process(target=gofood, args=(21,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()
    p17.start()
    p18.start()
    p19.start()
    p20.start()