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
for i in a:
    if i<=b and prime(i):
        c+=1
print(c)