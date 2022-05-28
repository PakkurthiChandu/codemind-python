a=input()
m=0
c=0
for i in range(0,len(a)-1):
    if a[i]==a[i+1]:
        c+=1
    if c>m:
        m=c
    if a[i]!=a[i+1]:
        c=0;
print(m+1)