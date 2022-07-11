a=input()
b='aeiou'
c='AEIOU'
d=0
e=0
for i in b:
    if i in a:
        d+=1
for i in c:
    if i in a:
        e+=1
if d==5 or e==5:
    print('True')
else:
    print('False')