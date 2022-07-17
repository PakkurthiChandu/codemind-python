n=int(input())
a=list(map(int,input().split()))
b=a[0:n//2]
c=a[n//2:n]
c=c[::-1]
i=0
j=0
while i<len(b) or j<len(c):
    if i<len(b):
        print(b[i],end=' ')
    if j<len(c):
        print(c[i],end=' ')
    i+=1
    j+=1
if n%2!=0:
    print('0')