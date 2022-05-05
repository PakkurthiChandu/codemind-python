def per(a):
    for i in range(1,a+1):
        if i*i==a:
            return 1
        elif i*i>a:
            return 0
n=int(input())
a=[n]
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    if per(a[i]):
        s+=a[i]
print(s)