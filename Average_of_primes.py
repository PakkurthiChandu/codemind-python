def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
b=0
s=0
for i in a:
    if prime(i):
        b+=1
        s+=i
print("%.2f"%(s/b))