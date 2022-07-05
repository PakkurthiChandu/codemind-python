def prime(a):
    if(a==1):
        return 0
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    return 1
a=int(input())
if prime(a):
    s=0
    c=0
    while a!=0:
        b=a%10
        a=a//10
        c+=1
        s+=prime(b)
    if(s==c):
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')