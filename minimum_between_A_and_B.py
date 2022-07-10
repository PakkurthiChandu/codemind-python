n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
m=99999999999999999
for i in a:
    if i>=b and i<=c:
        if i<m:
            m=i
if m==99999999999999999:
    print('-1')
else:
    print(m)