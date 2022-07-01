import threading
import time


def thread1():
    print("T1 start\n")
    for i in [3,2,1]:
        print(i)
        time.sleep(1)
    print("T1 all down\n")

def thread2():
    print("T2 start\n")
    for i in [5,4,3,2,1]:
        print(i)
        time.sleep(1)
    print("T2 all down\n")

def main():
    addedThread1=threading.Thread(target=thread1,name="T1")
    addedThread2=threading.Thread(target=thread2,name="T2")
    addedThread1.start()
    addedThread2.start()



    addedThread1.join() # join, it will wait for the subthread to execute completely and it will execute follow programs
    addedThread2.join()

    print("main finished\n")

if __name__ == '__main__':
    main()