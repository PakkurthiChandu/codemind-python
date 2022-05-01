n=int(input())
a=[n]
a=list(map(int,input().split()))
b=min(a)
c=0
for i in range(b,0,-1):
    for j in range(0,n):
        if a[j]%i!=0:
            c=1
    if c==0:
        print(i)
        break
    c=0
        