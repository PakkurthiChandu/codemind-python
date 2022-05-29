n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
m=0
for i in range(0,n):
    if a[i]<b or a[i]>c:
        if a[i]>m:
            m=a[i]
            s=1
if s==0:
    print("-1")
else:
    print(m)