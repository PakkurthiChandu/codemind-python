a=int(input())
n=len(str(a))
s=0
t=a
while a!=0:
    b=a%10
    a=a//10
    s+=b**n
    n-=1
if s==t:
    print('True')
else:
    print('False')