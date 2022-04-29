a=int(input())
f=0
s=1
b=0
c=0
while b<=a:
    b=f+s
    f=s
    s=b
    if f==a:
        c=1
if c==1:
    print('True')
else:
    print('False')