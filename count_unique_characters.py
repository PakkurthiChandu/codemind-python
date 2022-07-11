a=input().lower()
a=a.replace(" ","")
c=0
for i in a:
    if a.count(i)==1:
        c+=1
print(c)