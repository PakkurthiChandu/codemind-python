a=int(input())
f=0
s=1
print(f,end=' ')
print(s,end=' ')
for i in range(3,a+1):
    b=f+s
    print(b,end=' ')
    f=s
    s=b