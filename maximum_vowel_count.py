a=input()
a=a.split(' ')
m=0
b='aeiou'
for i in a:
    c=0
    for j in range(0,len(i)):
        if i[j] in b:
            c+=1
    if c>m:
        m=c
print(m)