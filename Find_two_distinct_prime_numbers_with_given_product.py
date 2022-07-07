def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
c=0
for i in range(1,a):
    if prime(i):
        for j in range(1,a):
            if prime(j):
                if i*j==a:
                    c=1
                    print(i,j)
                    break
                elif i*j>a:
                    break
    if c==1:
        break
else:
    print('-1')