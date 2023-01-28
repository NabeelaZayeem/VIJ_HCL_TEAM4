import threading
import time
from threading import *
#print(threading.current_thread().getName())
def demo_thread():
    time.sleep(2)
    print("Hello")
t1=Thread(target=demo_thread)
t1.start()