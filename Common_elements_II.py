a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in c:
    if i not in d:
        print(i,end=' ')
for i in d:
    if i not in c:
        print(i,end=' ')