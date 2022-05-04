def rev(a):
    r=0
    while a!=0:
        b=a%10
        a=a//10
        r=r*10+b
    return r
n=int(input())
a=[n]
b=[n]
a=list(map(int,input().split()))
from array import*
for i in range(0,n):
    x=rev(a[i])
    b.append(x)
for i in range(1,n+1):
    print(b[i],end=' ')