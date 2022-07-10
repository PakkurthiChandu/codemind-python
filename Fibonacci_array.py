n=int(input())
a=list(map(int,input().split()))
if n>=3:
    c=0
    for i in range(2,n):
        if a[i-1]+a[i-2]!=a[i]:
            c=1
    if c==0:
        print('yes')
    else:
        print('no')
else:
    print('no')