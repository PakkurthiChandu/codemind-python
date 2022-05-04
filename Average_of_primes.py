def prime(a):
    if a==1:
        return 0
    else:
        for i in range(2,a):
            if a%i==0:
                return 0
    return 1
n=int(input())
a=[n]
a=list(map(int,input().split()))
s=0
c=0
for i in range(0,n):
    if prime(a[i]):
        s+=a[i]
        c+=1
b=s/c
print("%.2f"%b)