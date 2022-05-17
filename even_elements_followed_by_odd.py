n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(0,n):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
for i in range(0,len(b)):
    print(b[i],end=' ')
for i in range(0,len(c)):
    print(c[i],end=' ')