a=input().lower()
b=''
a=a.split(' ')
for i in a[0]:
    c=0
    for j in a:
        if i in j:
            c+=1
    if c==len(a):
        b+=i
if len(b)==0:
    print('-1')
else:
    print(b)