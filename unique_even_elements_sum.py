n=int(input())
a=[n]
a=list(map(int,input().split()))
c=0
s=0
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]==a[j]:
            c+=1
    if c==0 and a[i]%2==0:
        s+=a[i]
    c=0
print(s)
            