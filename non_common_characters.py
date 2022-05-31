a=input().lower()
b=input().lower()
f=''
for i in range(0,len(a)):
    if a[i] not in b and a[i] not in f and a[i]!=' ':
        f+=a[i]
for i in range(0,len(b)):
    if b[i] not in a and b[i] not in f and b[i]!=' ':
        f+=b[i]
f=sorted(f)
for i in range(0,len(f)):
    print(f[i],end='')