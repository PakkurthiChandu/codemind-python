a=input().lower()
a=a.replace(" ","")
b=''
for i in a:
    if i not in b:
        b+=i
b=sorted(b)
for i in b:
    print(i,end='')