n=int(input())
a=[n]
a=list(map(int,input().split()))
c=0
k=0
for i in range(0,n):
    for j in range(0,n):
        if a[i]==a[j]:
            c+=1
    if c==1:
        if a[i]%2!=0:
            k+=1
    c=0
print(k)