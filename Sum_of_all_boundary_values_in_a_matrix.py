a,b=map(int,input().split())
c=[]
s=0
for i in range(a):
    d=list(map(int,input().split()))
    c.append(d)
for i in range(a):
    for j in range(b):
        if i==0 or i==a-1 or j==0 or j==b-1:
            s+=c[i][j]
print(s)