
import threading
from queue import Queue
import time


list =[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,12,12,12]]

def job(list,q):
    for i in range(len(list)):
        list[i] = list[i]**2
        time.sleep(1)
        print(f'through compute time is {i}')
    q.put(list)


def multithreading():
    q=Queue()
    threads=[]

    for i in range(4):
        thread=threading.Thread(target=job,args=(list[i],q))
        thread.start()
        threads.append(thread)

    for thread in threads:
        threads =thread.join()

    


    result=[]
    for i in range(4):
        result.append(q.get())
    

    print(result)
    print("We didn't wait 12 seconds to complete computing if we use multi-threding to compute")
if __name__ =="__main__":
    multithreading()