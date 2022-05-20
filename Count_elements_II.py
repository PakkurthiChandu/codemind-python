n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(set(a))
d=list(set(b))
e=0
for i in range(0,len(c)):
    if c[i] not in d:
        e+=1
for i in range(0,len(d)):
    if d[i] not in c:
        e+=1
print(e)