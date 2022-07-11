n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
m=9999999999999999
for i in a:
    if i<b or i>c:
        if i<m:
            m=i
if m==9999999999999999:
    print('-1')
else:
    print(m)