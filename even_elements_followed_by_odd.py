n=int(input())
a=list(map(int,input().split()))
e=[]
for i in range(0,n):
    if a[i]%2==0:
        e.append(a[i])
print(*e,end=' ')
for i in a:
    if i not in e:
        print(i,end=' ')