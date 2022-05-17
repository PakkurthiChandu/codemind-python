a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(0,a):
    if b[i]%2==0:
        c.append(b[i])
    else:
        d.append(b[i])
i=0
j=0
while(i<len(d) or j<len(c)):
    if i<len(d):
        print(d[i],end=' ')
    if j<len(c):
        print(c[i],end=' ')
    i+=1
    j+=1
if a%2!=0:
    print('0')