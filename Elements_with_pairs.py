n=int(input())
a=[n]
a=list(map(int,input().split()))
for i in range(0,n):
    print(a[i],end=' ')
if n%2!=0:
    print('0')