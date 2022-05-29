n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
m=9999999
d=0
for i in range(0,n):
    if a[i]>=b and a[i]<=c:
        if a[i]<m:
            m=a[i]
            d=1
if d==0:
    print("-1")
else:
    print(m)
