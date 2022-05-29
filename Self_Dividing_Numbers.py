def se(a):
    t=a
    c=0
    d=0
    while(a):
       b=a%10
       a=a//10
       if(b!=0 and t%b==0):
           d+=1
       c+=1
    if d==c:
        return 1
    return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if se(i):
        print(i,end=' ')