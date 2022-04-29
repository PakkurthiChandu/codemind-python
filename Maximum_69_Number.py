a=int(input())
r=0
rev=0
c=0
while a!=0:
    b=a%10
    a=a//10
    r=r*10+b
while r!=0:
    b=r%10
    r=r//10
    if c==0:
        if b==6:
            b=9
            c=1
    rev=rev*10+b
print(rev)
