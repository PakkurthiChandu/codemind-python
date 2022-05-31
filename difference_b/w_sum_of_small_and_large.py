a=input()
b=a.split(' ')
s=0
d=0
for i in range(0,len(b)):
    s+=ord(min(b[i]))
    d+=ord(max(b[i]))
print(abs(s-d))