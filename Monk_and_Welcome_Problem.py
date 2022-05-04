n=int(input())
a=[n]
b=[n]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(0,n):
    print(a[i]+b[i],end=' ')