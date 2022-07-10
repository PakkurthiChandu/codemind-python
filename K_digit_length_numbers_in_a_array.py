a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in range(0,a):
    if c[i]<0:
        c[i]=-c[i]
    if len(str(c[i]))==b:
        d+=1
print(d)