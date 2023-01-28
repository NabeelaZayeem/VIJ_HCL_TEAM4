from threading import *
import time
def wish(name):
    for i in range(10):
        print("Good Afternoon",end='')
        time.sleep(2)
        print(name)
t1=Thread(target=wish,args={'Nabeela'})
t2=Thread(target=wish, args={'Zayeem'})
t1.start()
t1.join()
t2.start()
