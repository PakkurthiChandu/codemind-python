a=input().lower()
b=input().lower()
c=''
f=0
d=list(set(a)&set(b))
for i in d:
    if i==' ':
        continue
    c+=i
    f=1
e=sorted(c)
if f==0:
    print('-1')
else:
    for i in e:
        print(i,end='')