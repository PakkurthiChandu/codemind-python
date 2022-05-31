a=input().lower()
b=a.split(' ')
e=0
d=''
for i in range(0,len(b[0])):
    c=0
    for j in range(0,len(b)):
        if b[0][i] in b[j]:
            c+=1
    if c==len(b):
        d+=b[0][i]
        e=1
if e==0:
    print('-1')
else:
    print(min(d))