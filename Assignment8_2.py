from threading import *;
def even(num):
    even_sum=0;
    for i in range(1,num+1):
        if ((i % 2) == 0):
            even_sum=even_sum+i;
    print("even_sum=",even_sum);

def odd(num):
    odd_sum=0;
    for i in range(num+1):
        if(not(i%2)==0):
            odd_sum=odd_sum+i;
    print("odd_sum=",odd_sum);

def main():
    no=10;
    t1=Thread(target=even,args=(no,));
    t2=Thread(target=odd,args=(no,));
    t1.start();
    t2.start();

if __name__=="__main__":
    main();




