a=int(input())
c=0
while a!=1:
    if a%2==0:
        a=a//2
    elif a%3==0:
        a=a//3
    elif a%5==0:
        a=a//5
    else:
        c=c+1
        break;
if c!=0:
    print('Not Ugly Number')
else:
    print('Ugly Number')