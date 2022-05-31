n=int(input())
a=list(map(int,input().split()))
if(n<=2):
    print('no')
else:
    for i in range(2,len(a)):
        if a[i]!=a[i-1]+a[i-2]:
            print('no')
            break
    else:
        print('yes')