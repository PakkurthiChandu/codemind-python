a,b=map(int,input().split())
c=max(a,b)
i=1
while(1):
    d=c*i
    if d%a==0 and d%b==0:
        print(d)
        break
    i+=1