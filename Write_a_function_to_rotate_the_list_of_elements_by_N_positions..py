n=int(input())
a=list(map(int,input().split()))
b=int(input())
while b>=n:
    b=b-n
for i in range(n-b,n):
    print(a[i],end=' ')
for i in range(0,n-b):
    print(a[i],end=' ')