def prime(a):
    if a==1:
        return 0
    else:
        for i in range(2,a):
            if a%i==0:
                return 0
    return 1
c=0
n=int(input())
a=[n]
a=list(map(int,input().split()))
for i in range(0,n):
    if prime(a[i]):
        c+=1
print(c)