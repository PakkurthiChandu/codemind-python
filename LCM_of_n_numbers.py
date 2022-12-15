n=int(input())
a=list(map(int,input().split()))
t=max(a)
for i in range(t,t+10000000):
    for k in a:
        if i%k!=0:
            break
    else:
        print(i)
        break