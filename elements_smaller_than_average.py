n=int(input())
a=list(map(int,input().split()))
b=sum(a)
b=b//n
c=0
for i in a:
    if i<=b:
        c+=1
print(c)