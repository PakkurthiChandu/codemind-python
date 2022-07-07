a=int(input())
f=0
s=1
t=0
while t<a:
    t=f+s
    f=s
    s=t
if t==a:
    print('True')
else:
    print('False')