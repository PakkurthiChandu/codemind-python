a=input()
b='aeiouAEIOU'
c=0
d=''
for i in a:
    if i in b:
        c=1
        if i not in d:
            d+=i
if c==0:
    print("-1")
else:
    print(*d)