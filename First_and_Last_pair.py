n=int(input())
a=[n]
a=list(map(int,input().split()))
j=n-1
for i in range(0,n//2):
    print(a[i],end=' ')
    print(a[j],end=' ')
    j-=1
if n%2!=0:
    print(a[n//2],end=' ')
    print('0',end=' ')