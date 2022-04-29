a=int(input())
b=int(input())
def pal(i):
    a=i
    r=0
    while i!=0:
        b=i%10
        i=i//10
        r=r*10+b
    if a==r:
        print(a,end=' ')
for i in range(a,b+1):
    pal(i)

