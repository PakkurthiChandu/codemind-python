def pal(a):
    b=str(a)
    b=b[::-1]
    b=int(b)
    return b
n=int(input())
a=list(map(int,input().split()))
d=0
for i in a:
    print(pal(i),end=' ')