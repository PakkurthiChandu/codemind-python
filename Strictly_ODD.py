n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    if i%2==0 and a[i]%2!=0:
        print('False')
        break
else:
    print('True')