n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n):
    b.append(max(a))
    a[a.index(max(a))]=0
for i in range(n-1,-1,-1):
    print(b[i],end=' ')