n,k=map(int,input().split())
a=[n]
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if a[i]%k!=0:
        c+=1
print(c)