a=int(input())
f=0
s=1
for i in range(3,a):
    b=f+s
    f=s
    s=b
    if b>a:
        break
if (a-f)<(s-a):
    print(f)
elif((a-f)==(s-a)):
    print(f,end=' ')
    print(s)
else:
    print(s)