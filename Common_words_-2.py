a=input().lower()
b=input().lower()
c=a.split(' ')
d=b.split(' ')
e=0
for i in range(0,len(c)):
    if c[i] in b and a.count(c[i])==b.count(c[i]):
        e+=1
print(e)