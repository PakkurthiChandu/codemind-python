n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in range(0,n):
    if a[i] not in b:
        b.append(a[i])
for i in range(0,len(b)):
    if a.count(b[i])==b[i]:
        print(b[i],end=' ')
        c+=1
if c==0:
    print('-1')