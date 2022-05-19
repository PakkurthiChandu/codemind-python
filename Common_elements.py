n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(0,n):
    if a[i] in b:
        c.append(a[i])
for i in range(0,len(c)):
    if c[i] not in d:
        d.append(c[i])
for i in range(0,len(d)):
    print(d[i],end=' ')