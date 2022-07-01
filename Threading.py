import threading

def threadJob():
    
    print("this job displays current thread, number is %s" %threading.currentThread())




def main():


    addedThread=threading.Thread(target=threadJob)
    addedThread.start()

    
    # to tell us how many threading
    print(threading.activeCount())
    # to tell us threading name   
    print(threading.enumerate())  #enumerate 列舉
    # to tell us currently execute threads 
    print(threading.currentThread())
    

if __name__ == '__main__':

    main()