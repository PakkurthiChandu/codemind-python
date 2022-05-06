n=int(input())
a=[n]
a=list(map(int,input().split()))
s=0
d=0
for i in range(0,n):
    if i%2==0:
        s+=a[i]
    else:
        d+=a[i]
if (s-d)==0:
    print('YES')
else:
    print('NO')