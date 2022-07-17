def pal(a):
    b=a[::-1]
    if b==a:
        return 1
    return 0
a=input().lower()
s=''
b=''
for i in range(len(a)):
    s=''
    for j in range(i,len(a)):
       s+=a[j]
       if pal(s) and len(s)>len(b):
           b=s
print(b)