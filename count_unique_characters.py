a=input().lower()
c=0
for i in range(0,len(a)):
    if a.count(a[i])==1 and a[i]!=' ':
        c+=1
print(c)