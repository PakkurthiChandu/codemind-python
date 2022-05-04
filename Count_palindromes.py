def pal(a):
    t=a
    r=0
    while a!=0:
        b=a%10
        a=a//10
        r=r*10+b
    if t==r:
        return 1
    else:
        return 0
n=int(input())
c=0
a=[n]
a=list(map(int,input().split()))
for i in range(0,n):
    if pal(a[i]):
        c+=1
print(c)
        