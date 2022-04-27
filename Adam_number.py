a=int(input())
b=a*a
rev=0
r=0
while a!=0:
    c=a%10
    a=a//10
    rev=rev*10+c
d=rev*rev
while d!=0:
    e=d%10
    d=d//10
    r=r*10+e
if r==b:
    print('True')
else:
    print('False')