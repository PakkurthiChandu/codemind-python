a=input().lower()
b='aeiou'
c=0
m=0
for i in a:
    if i in b:
        c+=1
    if c>m:
        m=c
    if i not in b:
        c=0
print(m)