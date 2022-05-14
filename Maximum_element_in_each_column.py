n,m=map(int,input().split())
b=[]
for i in range(0,n):
    a=list(map(int,input().split()))
    b.append(a)
for i in range(0,m):
    d=0
    for j in range(0,n):
        if b[j][i]>d:
            d=b[j][i]
    print(d)