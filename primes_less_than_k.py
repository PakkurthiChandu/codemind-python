def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
for i in range(0,n):
    if a[i]<=b and prime(a[i]):
        c+=1
print(c)