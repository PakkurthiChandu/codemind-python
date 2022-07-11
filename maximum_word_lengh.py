a=input()
a=a.split(' ')
m=len(a[0])
for i in a:
    if len(i)>m:
        m=len(i)
print(m)