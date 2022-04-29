a=int(input())
c=0
def pri(a):
    if a==1:
        return 0
    else :
        for i in range(2,a):
            if a%i==0:
                return 0
    return 1
for i in range (1,a+1):
    if a%i==0:
        if pri(i):
            pass
        else:
            c+=1
print(c)