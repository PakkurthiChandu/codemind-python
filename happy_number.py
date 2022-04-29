a=int(input())
s=0
while 1:
    while a!=0:
        b=a%10
        a=a//10
        s+=b*b
    if s==1 or s==7:
        print('True')
        c+=1
        break
    elif s<10:
        print('False')
        break
    else:
        a=s
        s=0

        