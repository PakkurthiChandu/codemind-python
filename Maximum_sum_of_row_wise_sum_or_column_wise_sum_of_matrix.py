n,m=map(int,input().split())
a=[]
s=0
d=0
e=0
for i in range(0,n):
    b=list(map(int,input().split()))
    if sum(b)>s:
        s=sum(b)
    a.append(b)
for i in range(0,m):
    for j in range(0,n):
        d+=a[j][i]
    if d>e:
        e=d
    e=0
if s>e:
    print(s)
else:
    print(e)