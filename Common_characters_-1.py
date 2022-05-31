a=input().lower()
b=a.split(' ')
d=0
for i in range(0,len(b[0])):
    c=0
    for j in range(0,len(b)):
        if b[0][i] in b[j]:
            c+=1
    if c==len(b):
        print(b[0][i],end='')
        d=1
if d==0:
    print('-1')