def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
b=str(a)
c=int(b[::-1])
if prime(a) and prime(c):
    print('circular prime')
elif prime(a) or prime(c):
    print('prime but not a circular prime')
else:
    print('not prime')