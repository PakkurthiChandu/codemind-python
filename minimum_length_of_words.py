a=input()
a=a.split(' ')
m=9999999999999999
for i in a:
    if len(i)<m:
        m=len(i)
print(m)