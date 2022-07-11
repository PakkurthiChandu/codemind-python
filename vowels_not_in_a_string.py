a=input().lower()
b='aeiou'
c=''
for i in a:
    if i in b:
        c+=i
d=0
for i in b:
    if i in c:
        d+=1
if d==5:
    print('0')
else:
    for i in b:
        if i not in c:
            print(i,end=' ')