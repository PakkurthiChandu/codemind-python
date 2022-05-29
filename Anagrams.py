a=input().lower()
b=input().lower()
c=0
d=0
for i in range(0,len(a)):
    if a[i] in b:
        c+=1
if c==len(b):
    print('True')
else:
    print('False')
    