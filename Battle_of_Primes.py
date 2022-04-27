a=int(input())
b=int(input())
c=a+b+1
te=c
while 1:
    t=c
    k=0
    for i in range(2,t):
        if t%i==0:
            k+=1
            break
    if k==0:
        #print(c)
        break
    c+=1
print("%d"%(c-te+1))
