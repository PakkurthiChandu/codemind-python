n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=list(b)
d=0
for i in range(0,len(c)):
    d+=a.count(c[i])//2
print(d)