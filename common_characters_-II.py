a=input().lower()
b=input().lower()
a=a.replace(" ",'')
b=b.replace(' ','')
c=''
for i in a:
    if i in b and i not in c:
        c+=i
c=sorted(c)
print(len(c))