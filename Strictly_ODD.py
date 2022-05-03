n=int(input())
a=[n]
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if a[i]%2!=0 and i%2==0:
        c+=1
if c==0:
    print('True')
else:
    print('False')