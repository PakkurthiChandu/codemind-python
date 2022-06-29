def sum_d(a):
    b=str(a)
    s=0
    for i in b:
        s+=int(i)
    return s
a=int(input())
while 1:
    a=sum_d(a)
    if a<10:
        print(a)
        break