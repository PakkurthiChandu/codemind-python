n=int(input())
a=[n]
c=0
a=list(map(int,input().split()))
for i in range(0,n):
    if a[i]%2==0 and i%2!=0:
        c+=1
if c==0:
    print('True')
else:
    print('False')