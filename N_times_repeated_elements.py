n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=[]
for i in a:
    if i not in c and a.count(i)==b:
        c.append(i)
if len(c)==0:
    print('-1')
else:
    print(*c)