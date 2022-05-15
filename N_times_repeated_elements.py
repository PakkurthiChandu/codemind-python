n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=list(set(a))
d=0
for i in range(0,len(c)):
    if a.count(c[i])==b:
        print(c[i],end=' ')
        d=1
if d==0:
    print('-1')