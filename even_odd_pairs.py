n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        e.append(a[i])
    else:
        o.append(a[i])
i=0
j=0
while i<len(e) or j<len(o):
    if i<len(e):
        print(e[i],end=' ')
    if j<len(o):
        print(o[j],end=' ')
    i+=1
    j+=1
if n%2!=0:
    print('0')