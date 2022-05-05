def per(a):
    for i in range(1,a):
        if i*i==a:
            return 1
        if i*i>a:
            return 0
n=int(input())
for i in range(0,n):
    b=int(input())
    if per(b):
        print('True')
    else:
        print('False')