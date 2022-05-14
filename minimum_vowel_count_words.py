a=list(map(str,input().split()))
m=99999999
for i in range(0,len(a)):
    s=a[i].count('a')+a[i].count('e')+a[i].count('i')+a[i].count('o')+a[i].count('u')
    if s<m:
        m=s
c=0
for i in range(0,len(a)):
    s=a[i].count('a')+a[i].count('e')+a[i].count('i')+a[i].count('o')+a[i].count('u')
    if s==m:
        c+=1
print(c)