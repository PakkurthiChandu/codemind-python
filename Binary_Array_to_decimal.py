n=int(input())
a=list(map(int,input().split()))
b=0
j=n-1
for i in a:
    b+=i*pow(2,j)
    j-=1
print(b)