def digi(a):
    if a=='I':
        return 1
    elif a=='V':
        return 5
    elif a=='X':
        return 10
    elif a=='L':
        return 50
    elif a=='C':
        return 100
    elif a=='D':
        return 500
    elif a=='M':
        return 1000
a=input()
n=digi(a[0])
for i in range(1,len(a)):
    if digi(a[i-1])<digi(a[i]):
        n=n-digi(a[i-1])+(digi(a[i])-digi(a[i-1]))
    else:
        n+=digi(a[i])
print(n)