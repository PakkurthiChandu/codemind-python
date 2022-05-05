n,s=map(int,input().split())
a=[n]
a=list(map(int,input().split()))
k=0
c=0
for i in range(0,n):
    for j in range(i,n):
        k+=a[j]
        if s==k:
            c+=1
        if k>s:
            k=0
            break
print(c)