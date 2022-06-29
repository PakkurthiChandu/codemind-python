def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
def pal(a):
    b=str(a)
    if a==int(b[::-1]):
        return 1
    return 0
a=int(input())
while 1:
    a+=1
    if pal(a) and prime(a):
        print(a)
        break