a,b=map(int,input().split())
c=0
for i in range(a):
    d=list(map(int,input().split()))
    e=[]
    for i in range(len(d)-1,-1,-1):
        e.append(d[i])
    if d==sorted(d) or e==sorted(d):
        c+=1
print(c)