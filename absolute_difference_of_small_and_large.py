a=input()
a=a.split(" ")
for i in range(0,len(a)):
    print(ord(max(a[i]))-ord(min(a[i])),end=' ')