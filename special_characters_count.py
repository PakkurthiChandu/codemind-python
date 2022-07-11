a=input()
c=0
for i in a:
    if (i>='A' and i<='Z') or (i>='0' and i<='9') or (i>='a' and i<='z') or i==' ':
        pass
    else:
        c+=1
print(c)