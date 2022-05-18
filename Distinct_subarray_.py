n=int(input())
m=int(input())
a=[]
for i in range(n,m+1):
    a.append(i)
c=0
s=0
for i in range(0,len(a)):
    for j in range(i,len(a)):
        s+=a[j]
        if s%2!=0:
            c+=1
    s=0
print(c)