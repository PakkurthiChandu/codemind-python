n=int(input())
a=[n]
a=list(map(int,input().split()))
for i in range(n-1,0,-1):
    if a[i]%2!=0:
        print(a[i])
        break