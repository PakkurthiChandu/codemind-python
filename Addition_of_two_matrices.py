n=int(input())
a=[]
b=[]
for i in range(n):
    d=list(map(int,input().split()))
    a.append(d)
for i in range(n):
    d=list(map(int,input().split()))
    b.append(d)
c=[]
for i in range(n):
    d=[]
    for j in range(n):
       d.append(a[i][j]+b[i][j]) 
    c.append(d)
for i in range(n):
    for j in range(n):
        if j==n-1:
            print(c[i][j])
        else:
            print(c[i][j],end=' ')