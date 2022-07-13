n=int(input())
for i in range(n):
    a=int(input())
    b=str(a)
    c=[]
    for i in b:
        c.append(int(i))
    d=max(c)
    e=min(c)
    for i in range(e,d+1):
        if i not in c:
            print('NO')
            break
    else:
        print('YES')