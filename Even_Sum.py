n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    if a[i]%2==0:
        s+=a[i]
print(s)