def dig(a):
    c=0
    while a!=0:
        b=a%10
        a=a//10
        c+=1
    return c
def au(a):
    c=dig(a)
    b=a*a
    k=0
    r=0
    rev=0
    while b!=0:
        k+=1
        d=b%10
        b=b//10
        r=r*10+d
        if k==c:
            break
        
    while r!=0:
        d=r%10
        r=r//10
        rev=rev*10+d
    if rev==a:
        return 1
    else:
        return 0
n=int(input())
if au(n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')