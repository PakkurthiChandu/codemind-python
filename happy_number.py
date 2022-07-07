a=int(input())
while a>9:
    t=a
    a=0
    while t!=0:
        b=t%10
        t=t//10
        a+=b*b
if a==1 or a==7:
    print('True')
else:
    print('False')