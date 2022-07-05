a=int(input())
i=1
while i*(i+1)<a:
    i+=1
if i*(i+1)==a:
    print('YES')
else:
    print('NO')