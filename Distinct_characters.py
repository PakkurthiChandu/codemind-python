a=input().lower()
b=''
for i in range(0,len(a)):
    if a.count(a[i])==1 and a[i]!=' ':
        b+=a[i]
b=sorted(b)
for i in range(0,len(b)):
    print(b[i],end='')