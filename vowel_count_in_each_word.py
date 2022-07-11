a=input()
a=a.split(' ')
b='aeiou'
for i in a:
    c=0
    for j in range(0,len(i)):
        if i[j] in b:
            c+=1
    print(c,end=' ')