a=int(input())
t=a
p=1
s=0
while a!=0:
    b=a%10
    a=a//10
    for i in range(b,0,-1):
        p*=i
    s+=p
    p=1
if t==s:
    print('The number',t,'is a strong number')
else:
     print('The number',t,'is not a strong number')
    