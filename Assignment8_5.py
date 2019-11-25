from threading import *

def printNum(lock):
    lock.acquire();
    for i in range(1,51):
        print(i,end=" ")
    lock.release();

def printReverseNum(lock):
    lock.acquire();
    print("Reverse numbers")
    for i in range(50,0,-1):
        print(i,end=" ")
    lock.release();

def main():
    lock = Lock()
    t1 = Thread(target=printNum, args=(lock,))
    t2 = Thread(target=printReverseNum, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__" :
    main();

