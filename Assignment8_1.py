from threading import *;

def Even(num):
  for i in range(1,num+1):
    if((i % 2) == 0):
     print("Even:",i)

def Odd(num):
  for i in range(1,num+1):
      if(not((i % 2) == 0)):
          print("Odd:",i)

def main():
    no = 10

    t1 = Thread(target=Even,args=(no,))
    t2 = Thread(target=Odd, args=(no,) )

    t1.start()
    t2.start()


if __name__ == "__main__":
    main()


