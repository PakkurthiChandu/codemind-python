n=int(input())
a=list(map(int,input().split()))
s=0
d=0
for i in range(0,n):
    if i%2==0:
        s+=a[i]
    else:
        d+=a[i]
if abs(s-d)%4==0:
    print('X')
else:
    print('Y')
        