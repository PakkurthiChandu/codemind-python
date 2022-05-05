a=input()
d=0
c=0
k=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c+=1
    if c==1:
        d+=1
    k+=1
    c=0
if k==d:
    print('Unique Number')
else:
    print('Not Unique Number')