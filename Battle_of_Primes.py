def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=a+b
while 1:
    c+=1
    if prime(c):
        print(c-(a+b))
        break
