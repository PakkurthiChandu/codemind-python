a,b=map(int,input().split())
s=0
for i in range(0,a):
    d=list(map(int,input().split()))
    s+=sum(d)
print(s)