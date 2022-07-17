a=input()
v='AEIOUaeiou'
a=a.split()
c=0
for i in a:
    j=0
    k=len(i)-1
    while j<=k:
        if (i[j] in v and i[k] not in v) or (i[j] not in v and i[k] in v):
            c+=1
        j+=1
        k-=1
print(c)