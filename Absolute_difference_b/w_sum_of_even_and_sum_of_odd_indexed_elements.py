n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,n,2):
    s+=a[i]
b=sum(a)-s
print(abs(b-s))