a=input().lower()
a=a.split(' ')
c=0
for i in a:
    b=i[::-1]
    if b==i:
        c+=1
print(c)