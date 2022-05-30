a=input()
b=''
for i in range(0,len(a)):
    if a[i]>='0' and a[i]<='9' and a[i] not in b:
        b+=a[i]
b=sorted(b)
c=''
d=0
for i in range(0,len(b)):
    if int(b[i])%2==0:
        c+=b[i]
        d+=1
        break
if(d==0):
    print('-1')
else:
    for i in range(0,len(b)):
        if b[i] not in c:
            c+=b[i]
    r=0
    for i in range(len(c)-1,-1,-1):
        r=r*10+int(c[i])
    print(r)
