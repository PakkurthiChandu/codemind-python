a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
c=list(set(c))
e=0
for i in c:
    if i in d:
        e+=1
print(e)