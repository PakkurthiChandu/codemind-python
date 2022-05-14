n=int(input())
a=list(map(int,input().split()))
r=0
for i in range(0,n):
    r=r*10+a[i]
b=str(r+1)
for i in range(0,len(b)):
    print(b[i],end=' ')