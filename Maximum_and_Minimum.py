n=int(input())
a=list(map(int,input().split()))
m=99999999999
ma=0
for i in a:
    if a.count(i)==i:
        if i<m:
            m=i
        if i>ma:
            ma=i
if m==99999999999 or ma==0:
    print('-1')
else:
    print(m,ma)