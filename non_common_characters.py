a=input().lower()
b=input().lower()
a=a.replace(" ","")
b=b.replace(" ","")
c=''
for i in a:
    if i not in b and i not in c:
        c+=i
for i in b:
    if i not in a and i not in c:
        c+=i
c=sorted(c)
for i in c:
    print(i,end='')