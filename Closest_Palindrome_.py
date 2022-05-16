def pal(a):
    t=a
    r=0
    while a!=0:
        b=a%10
        a=a//10
        r=r*10+b
    if r==t:
        return 1
    else:
        return 0
a=int(input())
for i in range(a+1,a+100):
    if pal(i):
        break
for j in range(a-1,a-100,-1):
    if pal(j):
        break
if (i-a)>(a-j):
    print(j)
elif (i-a)==(a-j):
    print(j,i)
else:
    print(i)