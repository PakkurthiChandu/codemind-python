n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
for i in range(0,3):
    if a[i]>b[i]:
        c+=a[i]-b[i]
    else:
        d+=b[i]-a[i]
if(d-c)<0:
    print(0)
else:
    print(d-c)