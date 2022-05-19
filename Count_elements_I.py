n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(set(a))
d=str(set(b))
e=0
for i in range(0,len(c)):
    if c[i] in b:
        e+=1
print(e)