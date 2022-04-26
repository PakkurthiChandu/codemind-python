a=int(input())
max=0
while a!=0:
    b=a%10
    a=a//10
    if b>max:
        max=b
print(max)