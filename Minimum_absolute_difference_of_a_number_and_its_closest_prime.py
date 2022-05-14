def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
for i in range(a,a+100):
    if prime(i):
        break
for j in range(a,a-100,-1):
    if prime(j):
        break
if (a-j)<=(i-a):
    print(a-j)
else:
    print(i-a)