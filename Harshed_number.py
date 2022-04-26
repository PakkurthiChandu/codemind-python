a=int(input())
s=0
t=a
while a!=0:
    b=a%10
    a=a//10
    s+=b
if t%s==0:
    print('True')
else :
    print('False')