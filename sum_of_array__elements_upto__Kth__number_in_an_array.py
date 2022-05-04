n=int(input())
a=[n]
a=list(map(int,input().split()))
se=int(input())
s=0
for i in range(0,n):
    s+=a[i]
    if a[i]==se:
        break
print(s)