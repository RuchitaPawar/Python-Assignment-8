from threading import *;

def countSmallChar(value,lock):
    lock.acquire();
    smallChar =0 ;
    for i in range(len(value)):
        if((value[i] >= 'a') and (value[i] <= 'z') ):
            smallChar = smallChar + 1;
    print("Count of small characters:",smallChar);
    lock.release();

def countCapChar(value,lock):
    lock.acquire();
    capChar = 0;
    for i in range(len(value)):
        if ((value[i] >= 'A') and (value[i] <= 'Z')):
          capChar = capChar + 1;
    print("Count of Capital characters:", capChar);
    lock.release();

def countDigit(value,lock):
    lock.acquire();
    digit = 0
    for i in range(len(value)):
     if ((value[i] >= '0') and (value[i] <= '9')):
        digit = digit + 1;
    print("Count of digits:", digit);
    lock.release();

def main():
  arg = input("Enter input:");

  lock = Lock()

  small = Thread(target=countSmallChar,args=(arg,lock))
  print("Small character counting thread name and id is:",small.getName(),small.ident)
  small.start()


  capital = Thread(target=countCapChar,args=(arg,lock))
  print("capital character counting thread name and id is:",capital.getName(),capital.ident)
  capital.start()

  digit = Thread(target=countDigit, args=(arg,lock))
  print("digit counting thread name and id is:", digit.getName(), digit.ident)
  digit.start()

  small.join()
  capital.join()
  digit.join()

if __name__ == "__main__" :
    main();

