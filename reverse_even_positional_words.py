a=list(map(str,input().split()))
for i in range(0,len(a)):
    if i%2==0:
        print(a[i][::-1],end=' ')
    else:
        print(a[i],end=' ')