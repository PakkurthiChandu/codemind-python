a=input().lower()
b=input().lower()
a=a.replace(" ",'')
b=b.replace(' ','')
c=''
for i in a:
    if i in b and i not in c:
        c+=i
c=sorted(c)
if len(c)==0:
    print('-1')
else:
    for i in c:
        print(i,end='')