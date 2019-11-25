from threading import *;
def even(evenList):
    even_sum=0;
    for i in range(len(evenList)):
        if ((evenList[i] % 2) == 0):
            even_sum=even_sum+evenList[i];
    print("even_sum=",even_sum);

def odd(oddList):
    odd_sum=0;
    for i in range(len(oddList)):
        if(not(oddList[i]%2)==0):
            odd_sum=odd_sum+oddList[i];
    print("odd_sum=",odd_sum);

def main():
    arr = list();
    no=int(input("enter toatl number of elements:"));

    print("Enter the elements:");
    for i in range(no):
        val = int(input())
        arr.append(val)


    t1=Thread(target=even,args=(arr,));
    t2=Thread(target=odd,args=(arr,));
    t1.start();
    t2.start();

if __name__=="__main__":
    main();




