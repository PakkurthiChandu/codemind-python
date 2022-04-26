a=int(input())
c=0
for i in range(1,a):
    p=i*(i+1)
    if p==a:
        c+=1
    if p>a:
        break
if c!=0:
    print('YES')
else:
    print('NO')
