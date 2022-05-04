def dig(a):
    s=0
    while a!=0:
        b=a%10
        a=a//10
        s+=b
    return s
n=int(input())
a=[n]
a=list(map(int,input().split()))
s=0
for i in range(0,n):
    s+=dig(a[i])
print(s)