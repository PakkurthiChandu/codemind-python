n=int(input())
a=[n]
a=list(map(int,input().split()))
s=0
c=0
for i in range(0,n//2):
    s+=a[i]
for i in range(n//2,n):
    c+=a[i]
print(s)
print(c)