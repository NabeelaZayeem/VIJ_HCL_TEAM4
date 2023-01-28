import time
from threading import *
s=Semaphore(2)
def wish(name):
    s.acquire()
    for i in range(10):
        print("Good evening",end='')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish, args=('Nabeela',))
t2=Thread(target=wish, args=('Zayeem',))
t3=Thread(target=wish, args=('Saniya',))
t4=Thread(target=wish, args=('Zak',))
t5=Thread(target=wish, args=('Zuff',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()