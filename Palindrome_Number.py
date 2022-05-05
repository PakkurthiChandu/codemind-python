def pal(a):
    t=a
    r=0
    while a!=0:
        b=a%10
        a=a//10
        r=r*10+b
    if r==t:
        return 1
    else:
        return 0
n=int(input())
for i in range(0,n):
    a=int(input())
    if pal(a):
        print('True')
    else:
        print('False')