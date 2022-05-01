a=int(input())
def d(a):
    d=0
    c=0
    while a!=0:
        b=a%10
        a=a//10
        if b%2==0:
            c+=1
        else:
            d+=1
    if d!=0 and c!=0:
        return 0
    elif c!=0 and d==0:
        return 1
    elif c==0 and d!=0:
        return 2
b=d(a)
if b==0:
    print('Mixed')
elif b==1:
    print('Even')
elif b==2:
    print('Odd')