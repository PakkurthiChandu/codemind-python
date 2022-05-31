a=input()
b=a.split(' ')
for i in range(0,len(b)):
    s=0
    d=0
    s+=ord(min(b[i]))
    d+=ord(max(b[i]))
    print(abs(s-d),end=' ')