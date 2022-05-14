n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(0,n):
    if a.count(a[i])==1:
        if a[i]>m:
            m=a[i]
if m==0:
    print('-1')
else:
    print(m)