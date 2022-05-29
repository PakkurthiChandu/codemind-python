n=int(input())
a=list(map(int,input().split()))
c=list(set(a))
s=0
d=0
for i in range(0,len(c)):
    if a.count(c[i])==c[i]:
        s+=c[i]
        d+=1
if d==0:
    print('-1')
else:
    print("%.2f"%(s/d))