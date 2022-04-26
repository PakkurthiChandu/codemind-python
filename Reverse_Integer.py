a=int(input())
rev=0
c=0
if a<0:
    a=-1*a
    c+=1
while a!=0:
    b=a%10
    a=a//10
    rev=rev*10+b
if(c==0):
    print(rev)
else:
    print(-1*rev)

