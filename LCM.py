a,b=map(int,input().split())
c=max(a,b)
d=min(a,b)
for i in range(1,d+1):
    e=c*i
    if e%a==0 and e%b==0:
        print(e)
        break;
    