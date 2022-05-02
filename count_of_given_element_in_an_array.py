n=int(input())
a=[n]
a=list(map(int,input().split()))
se=int(input())
c=0
for i in range(0,n):
    if a[i]==se:
        c+=1
print(c)