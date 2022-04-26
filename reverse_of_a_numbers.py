a=int(input())
rev=0
while a!=0:
    b=a%10
    a=a//10
    rev=rev*10+b
print(rev)
    