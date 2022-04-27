a=int(input())
r=0
t=a
te=a
s=0
i=0
while a!=0:
    b=a%10
    a=a//10
    r=r*10+b
    i+=1
while t!=0:
    c=t%10
    t=t//10
    s+=pow(c,i)
    i-=1
if te==s:
    print('True')
else:
    print('False')

