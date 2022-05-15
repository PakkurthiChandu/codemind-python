n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
c=0
for i in range(0,len(b)):
    if b[i]%2==0:
        c+=1
print(c)