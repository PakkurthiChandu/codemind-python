n,m=map(int,input().split())
a=[]
e=0
for i in range(n):
    b=list(map(int,input().split()))
    c=sorted(b)
    d=[]
    for i in range(len(c)-1,-1,-1):
        d.append(c[i])
    if b==c or d==b:
        e+=1
print(e)