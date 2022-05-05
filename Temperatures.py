n=int(input())
a=[n]
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(i+1,n):
        c+=1
        if a[i]<a[j]:
            break
    else:
        c=0
    print(c,end=' ')
    c=0
            