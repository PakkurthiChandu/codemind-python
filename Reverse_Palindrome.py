a=int(input())
def pal(a):
    t=a
    r=0
    while a!=0:
        b=a%10
        a=a//10
        r=r*10+b
    if t==r:
        return 1
    else:
        return 0
def rev(a):
    r=0
    while a!=0:
        b=a%10
        a=a//10
        r=r*10+b
    return r
while 1:
    a+=rev(a)
    if pal(a):
        print(a)
        break