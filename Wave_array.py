n=int(input())
a=list(map(int,input().split()))
if a[0]<a[1]:
    for i in range(1,n-1,2):
        if a[i]<a[i-1] or a[i]<a[i+1]:
            print('no')
            break
    else:
        print('yes')
else:
    for i in range(1,n-1,2):
        if a[i]>a[i-1] or a[i]>a[i+1]:
            print('no')
            break
    else:
        print('yes')