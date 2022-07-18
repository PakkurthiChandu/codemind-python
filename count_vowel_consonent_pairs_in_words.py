a=input()
a=a.split()
v='aeiouAEIOU'
c=0
for i in a:
    j=len(i)-1
    k=0
    while k<=j:
        if (i[k] in v and i[j] not in v) or (i[k] not in v and i[j] in v):
            c+=1
        j-=1
        k+=1
print(c)
            
        