n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(0,n-1):
    if a[i]>=a[i+1]:
        b=1
if b==0:
    print('yes')
else:
    print('no')