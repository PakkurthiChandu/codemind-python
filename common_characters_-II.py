a=input().lower()
b=input().lower()
f=''
for i in range(0,len(a)):
    if a[i] in b and a[i] not in f and a[i]!=' ':
        f+=a[i]
for i in range(0,len(b)):
    if b[i] in a and b[i] not in f and b[i]!=' ':
        f+=b[i]
print(len(f))