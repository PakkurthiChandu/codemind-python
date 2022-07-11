a=input().lower()
a=a.split(' ')
b='aeiou'
m=0
for i in a:
    c=0
    for j in range(0,len(i)):
        if i[j] in b:
            c+=1
    if c>m:
        m=c
d=0
for i in a:
    c=0
    for j in range(0,len(i)):
        if i[j] in b:
            c+=1
    if c==m:
        d+=1
print(d)