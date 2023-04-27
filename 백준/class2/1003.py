import sys
T = int(input())

zcnt = 0
ocnt = 0

def fibo(n):
    if(n==0):
        global zcnt 
        zcnt = zcnt+ 1
        return 0
    elif(n==1):
        global ocnt 
        ocnt = ocnt+1
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


for _ in range(T):
    n = int(sys.stdin.readline())
    fibo(n)
    print(zcnt, end = " ")
    print(ocnt)
    zcnt = 0
    ocnt = 0


