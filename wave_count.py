n=int(input())
a=list(map(int,input().split()))
if a[0]<a[1]:
    d=0
    c=0
    for i in range(1,n-1,2):
        if a[i-1]>a[i] or a[i]<a[i+1]:
            d=1
            break
        c+=1
    if d==1:
        print('-1')
    else:
        print(c)
else:
    d=0
    c=0
    for i in range(1,n-1,2):
        if a[i-1]<a[i] or a[i]>a[i+1]:
            d=1
            break
        c+=1
    if d==1:
        print('-1')
    else:
        print(c)