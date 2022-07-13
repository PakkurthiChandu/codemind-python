n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
c=[]
for i in b:
    c.append(i)
    c.append(a.count(i))
print(*c)