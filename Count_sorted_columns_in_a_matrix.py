a,b=map(int,input().split())
c=[]
for i in range(a):
   d=list(map(int,input().split())) 
   c.append(d)
g=0
for i in range(b):
    e=[]
    for j in range(a):
        e.append(c[j][i])
    f=[]
    for j in range(len(e)-1,-1,-1):
        f.append(e[j])
    if e==sorted(e) or f==sorted(e):
        g+=1
print(g)