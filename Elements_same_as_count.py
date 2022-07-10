n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
c=0
for i in b:
    if a.count(i)==i:
        print(i,end=' ')
        c=1
if c==0:
    print('-1')