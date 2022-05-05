a=int(input())
p=1
s=0
while a!=0:
    b=a%10
    a=a//10
    p*=b
    s+=b
print(p-s)