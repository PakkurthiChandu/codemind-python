n=int(input())
for i in range(n):
    k=int(input())
    a=list(map(int,input().split()))
    c=0
    for j in range(0,k):
        for l in range(0,k):
            if j==l:
                pass
            else:
                b=a[j]+a[l]
                if b in a:
                    c+=1
    if c==0:
        print('-1')
    else:
        print(c//2)