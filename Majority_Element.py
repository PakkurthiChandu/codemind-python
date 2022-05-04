n=int(input())
a=[n]
a=list(map(int,input().split()))
c=0
f=0
m=0
for i in range(0,n):
    for j in range(0,n):
        if a[i]==a[j]:
            c+=1
    if c>m:
        m=c
        f=a[i]
    c=0
print(f)