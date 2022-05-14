n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
f=-1
s=-1
for i in range(0,len(a)):
    if a[i]==b and c==0:
        f=i
        c=1
    if a[i]==b:
        s=i
print(f,s)