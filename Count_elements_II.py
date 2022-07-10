a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
c=list(set(c))
d=list(set(d))
e=0
for i in c:
    if i not in d:
        e+=1
for i in d:
    if i not in c:
        e+=1
print(e)