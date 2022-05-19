n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(0,n):
    if a[i] not in b:
        print(a[i],end=' ')
for i in range(0,m):
    if b[i] not in a:
        print(b[i],end=' ')