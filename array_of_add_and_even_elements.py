n=int(input())
a=list(map(int,input().split()))
o=[]
for i in range(0,n):
    if a[i]%2!=0:
        o.append(a[i])
print(*o,end=' ')
for i in a:
    if i not in o:
        print(i,end=' ')