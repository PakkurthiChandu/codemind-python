a=int(input())
c=0
for i in range(1,a):
    if i*i==a:
        print('True')
        c=1
        break
    if i*i>a:
        break
if c==0:
    print('False')