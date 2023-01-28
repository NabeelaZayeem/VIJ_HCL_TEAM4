import multiprocessing as mp
import math
from  time import perf_counter
#print(mp.cpu_count())1
result1=[]
result2=[]
def cal_one(number):
    for i in number:
        result1.append(math.sqrt(i**3))
        #print(result1)
def cal_two(number):
    for i in number:
        result2.append(math.sqrt(i**5))

if __name__=='__main__':
    numlist=list(range(2500000))
    p1=mp.Process(target=cal_one,args=(numlist,))
    p2=mp.Process(target=cal_two,args=(numlist,))
    start=perf_counter()
    p1.start()
    p2.start()
    end=perf_counter()
    print(f'{end-start} seconds taken')


