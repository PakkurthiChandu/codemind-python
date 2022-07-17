a,b=map(int,input().split())
c=[]
s=0
e=[]
for i in range(a):
    d=list(map(int,input().split()))
    c.append(d)
for i in range(a):
    s+=c[i][i]
    r=i
    r=r*10+i
    e.append(r)
j=b-1
for i in range(a):
    r=i
    r=r*10+j
    if r not in e:
        s+=c[i][j]
    j-=1
print(s)