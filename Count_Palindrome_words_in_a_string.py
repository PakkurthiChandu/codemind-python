def pal(a):
    b=a[::-1]
    if a==b:
        return 1
    return 0
a=input().lower()
a=a.split()
c=0
for i in a:
    if pal(i):
        c+=1
print(c)