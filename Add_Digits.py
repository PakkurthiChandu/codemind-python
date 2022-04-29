a=int(input())
s=0
while 1:
    while a!=0:
        b=a%10
        a=a//10
        s+=b
    if s<10:
        print(s)
        break
    else:
        a=s
        s=0