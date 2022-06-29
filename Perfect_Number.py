a=int(input())
s=0
for i in range(2,a//2+1):
    if a%i==0:
        s+=i
if a==(s+1):
    print('True')
else:
    print('False')
