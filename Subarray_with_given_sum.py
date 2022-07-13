n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    for i in range(0,a):
        s=0
        d=0
        for j in range(i,a):
            s+=c[j]
            if s>b:
                break
            if(s==b):
                d=1
                print(i+1,j+1)
                break
        if d==1:
            break
    else:
        print('-1')