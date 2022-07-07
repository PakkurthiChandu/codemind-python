def pal(a):
    b=str(a)
    b=b[::-1]
    b=int(b)
    if a==b:
        return 1
    else:
        return 0
a=int(input())
for i in range(a-1,a-100,-1):
    if pal(i):
        break
for j in range(a+1,a+100):
    if pal(j):
        break
if (a-i)==(j-a):
    print(i,j)
elif (a-i)<(j-a):
    print(i)
else:
    print(j)