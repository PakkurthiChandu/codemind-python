def pal(a):
    b=str(a)
    b=b[::-1]
    b=int(b)
    if a==b:
        return 1
    return 0
n=int(input())
a=list(map(int,input().split()))
d=0
for i in a:
    d+=pal(i)
print(d)