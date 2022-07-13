n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
d=[]
while len(b):
    m=0
    for i in b:
        c=a.count(i)
        if c>m:
            m=c
            t=b.index(i)
    d.append(b[t])
    b.pop(t)
print(*d)