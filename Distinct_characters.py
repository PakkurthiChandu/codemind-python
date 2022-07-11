a=input().lower()
a=a.replace(" ","")
b=''
for i in a:
    if a.count(i)==1:
        b+=i
b=sorted(b)
for i in b:
    print(i,end='')