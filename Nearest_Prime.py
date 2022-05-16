def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
n=int(input())
for i in range(0,n):
    a=int(input())
    for j in range(a,a-20,-1):
        if prime(j):
            break
    for k in range(a,a+20):
        if prime(k):
            break
    if (a-j)<=(k-a):
        print(j)
    else:
        print(k)