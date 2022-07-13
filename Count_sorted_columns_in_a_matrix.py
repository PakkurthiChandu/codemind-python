n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
g=0
for i in range(m):
    d=[]
    for j in range(n):
       d.append(a[j][i])
    e=sorted(d)
    f=[]
    for j in range(len(d)-1,-1,-1):
       f.append(e[j])
    if e==d or d==f:
        g+=1
print(g)
        
