n=int(input())
a=list(map(int,input().split()))
s=int(input())
for i in range(0,n):
    if (a[i]+s)>=max(a):
        print('True',end=' ')
    else:
        print('False',end=' ')