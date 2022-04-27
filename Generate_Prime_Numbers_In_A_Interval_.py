a=int(input())
b=int(input())
if a==1:
    a=a+1
c=0
for i in range(a,b):
    for j in range(2,i):
        if i%j==0:
            c+=1
            break
    if c==0:
        print(i)
    c=0