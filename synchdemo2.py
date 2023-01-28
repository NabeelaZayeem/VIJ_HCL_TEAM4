#LOCK
from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print('Good Evening',end='')
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args=('Nabeela',))
t2=Thread(target=wish,args=('Zayeem',))
t3=Thread(target=wish,args=('Mirza',))
t1.start()
t2.start()
t3.start()
