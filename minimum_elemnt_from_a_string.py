a=input()
c=a
a=a.split(' ')
b=min(a[len(a)-1])
if b.lower() in c:
    print(b.lower())
else:
    print(b)
    