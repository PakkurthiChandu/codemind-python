a=input()
b=''
c=''
d=0
for i in range(0,len(a)):
    if a[i]>='0' and a[i]<='9':
        if int(a[i])%2==0:
            b+=a[i]
        else:
            c+=a[i]
    if (a[i]>='0' and a[i]<='9') or (a[i]>='a' and a[i]<='z') or (a[i]>='A' and a[i]<='Z'):
        continue
    else:
        d+=1
i=0
j=0
if d%2==0:
    while(i<len(b) or j<len(c)):
        if i<len(b):
            print(int(b[i]),end='')
        if j<len(c):
            print(int(c[j]),end='')
        i+=1
        j+=1
else:
    while(i<len(b) or j<len(c)):
        if j<len(c):
            print(int(c[j]),end='')
        if i<len(b):
            print(int(b[i]),end='')
        i+=1
        j+=1
    