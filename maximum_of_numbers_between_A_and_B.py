n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
m=-1
for i in a:
    if i>=b and i<=c:
        if i>m:
            m=i
print(m)