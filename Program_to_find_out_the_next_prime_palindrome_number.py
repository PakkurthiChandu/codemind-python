a=int(input())
def prime(a):
    #import math
    #b=math.sqrt(a)
    if a==1:
        return 0
    else:
        for i in range(2,a//2):
            if a%i==0:
                return 0
    return 1
def pal(a):
    t=a
    r=0
    while a!=0:
        b=a%10
        a=a//10
        r=r*10+b
    if r==t:
        return 1
    return 
while 1:
    a+=1
    if pal(a):
        if prime(a):
            print(a)
            break