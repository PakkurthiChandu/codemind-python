def prime(a):
    if a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0 and prime(i)==0:
        c+=1
print(c)