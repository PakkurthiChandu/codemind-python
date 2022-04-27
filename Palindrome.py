a=int(input())
rev=0
t=a
while a!=0:
    b=a%10
    a=a//10
    rev=rev*10+b
if t==rev:
    print('True')
else:
    print('False')