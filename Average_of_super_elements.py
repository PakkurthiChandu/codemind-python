n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
s=0
c=0
for i in b:
    if a.count(i)==i:
        s+=i
        c+=1
if c==0:
    print('-1')
else:
    print("%.2f"%(s/c))